from io import BytesIO

from flask import flash, json, redirect, render_template, request, send_file, session

from database_service import DatabaseService
from content import combine_language_items, content
from db_util import truncate_db, source_exists_by_key, source_exists_by_id
from entities.article import Article
from entities.book import Book
from entities.inproceedings import Inproceedings
from entities.tag import Tag
from form_fields import get_fields_json
from config import app
from repositories.article_repository import ArticleRepository
from repositories.book_repository import BookRepository
from repositories.inproceedings_repository import InproceedingsRepository
from repositories.source_repository import SourceRepository
from repositories.tag_repository import TagRepository
from util import UserInputError, first_item, to_bibtex


@app.route("/", methods=["GET"])
def index_get():
    show_add_form = "show_add_form" in request.args
    form_json = get_fields_json()
    source_repo = SourceRepository(DatabaseService())
    lang = session.get("lang", "fi")

    try:
        sources = source_repo.get()
        return render_template(
            "index.html",
            sources=sources,
            form_json=form_json,
            show_add_form=show_add_form,
            lang=lang,
            saved_fields_json=session.get("fields", "{}"),
            content=content,
            content_json=json.dumps(content),
        )
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            content["error_common"][lang],
            "error",
        )
        print(error)
        return render_template(
            "index.html",
            content=content,
            content_json=json.dumps(content),
        )


@app.route("/edit/<int:source_id>", methods=["GET"])
def edit(source_id):
    source_repo = SourceRepository(DatabaseService())
    lang = session.get("lang", "fi")

    source = first_item(source_repo.get_full(source_id))

    if not source:
        flash(content["source_not_found"][lang], "error")
        return redirect("/")

    session["fields"] = json.dumps(source.__dict__)
    print(session["fields"])

    return redirect(f"/?show_add_form&edit_id={source_id}")


@app.route("/", methods=["POST"])
def index_post():
    form = request.form
    lang = session.get("lang", "fi")

    session["fields"] = json.dumps(form)

    source_type = form["kind"] if "kind" in form else ""
    bibtex_key = form["bibtex_key"] if "bibtex_key" in form else ""
    source_id = form["edit_id"] if "edit_id" in form else 0

    editing = "edit_id" in form

    error_redirect_path = "/?show_add_form" + (
        f"&edit_id={source_id}" if editing else ""
    )

    if not editing and len(bibtex_key) == 0:
        flash(
            combine_language_items(content["bibtex_key"], content["is_required"])[lang],
            "error",
        )
        return redirect(error_redirect_path)

    if not editing and source_exists_by_key(bibtex_key):
        flash(content["error_key_in_use"][lang], "error")
        return redirect(error_redirect_path)

    if editing and not source_exists_by_id(source_id):
        flash(content["error_source_not_found"][lang], "error")
        return redirect(error_redirect_path)

    book_repo = BookRepository(DatabaseService())
    article_repo = ArticleRepository(DatabaseService())
    inproceedings_repo = InproceedingsRepository(DatabaseService())

    try:
        match source_type:
            case "book":
                book = Book(
                    {
                        "source_id": source_id,
                        "bibtex_key": bibtex_key,
                        "title": form["title"] if "title" in form else "",
                        "year": form["year"] if "year" in form else "",
                        "author": form["author"] if "author" in form else "",
                        "source_book_id": 0,
                        "publisher": form["publisher"] if "publisher" in form else "",
                    }
                )

                if editing:
                    book_repo.update(book)
                else:
                    book_repo.create(book)

            case "article":
                article = Article(
                    {
                        "source_id": source_id,
                        "bibtex_key": bibtex_key,
                        "title": form["title"] if "title" in form else "",
                        "year": form["year"] if "year" in form else "",
                        "author": form["author"] if "author" in form else "",
                        "source_article_id": 0,
                        "journal": form["journal"] if "journal" in form else "",
                        "volume": form["volume"] if "volume" in form else "",
                        "number": form["number"] if "number" in form else "",
                        "pages": form["pages"] if "pages" in form else "",
                        "month": form["month"] if "month" in form else "",
                    }
                )

                if editing:
                    article_repo.update(article)
                else:
                    article_repo.create(article)

            case "inproceedings":
                inproceedings = Inproceedings(
                    {
                        "source_id": source_id,
                        "bibtex_key": bibtex_key,
                        "title": form["title"] if "title" in form else "",
                        "year": form["year"] if "year" in form else "",
                        "author": form["author"] if "author" in form else "",
                        "source_inproceedings_id": (
                            form["source_inproceedings_id"]
                            if "source_inproceedings_id" in form
                            else ""
                        ),
                        "booktitle": form["booktitle"] if "booktitle" in form else "",
                        "editor": form["editor"] if "editor" in form else "",
                        "series": form["series"] if "series" in form else "",
                        "pages": form["pages"] if "pages" in form else "",
                        "address": form["address"] if "address" in form else "",
                        "month": form["month"] if "month" in form else "",
                        "organization": (
                            form["organization"] if "organization" in form else ""
                        ),
                        "publisher": form["publisher"] if "publisher" in form else "",
                        "volume": form["volume"] if "volume" in form else "",
                    }
                )

                if editing:
                    inproceedings_repo.update(inproceedings)
                else:
                    inproceedings_repo.create(inproceedings)

            case _:
                flash(content["error_not_supported"][lang], "error")
                return redirect("/?show_add_form")

        clear_session()
        flash(content["msg_success"][lang], "success")
        return redirect("/")

    except UserInputError as error:
        flash(error.lang(lang), "error")
        return redirect(error_redirect_path)

    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            content["error_common"][lang],
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/delete/<int:source_id>", methods=["POST"])
def delete_source(source_id):
    source_repo = SourceRepository(DatabaseService())
    lang = session.get("lang", "fi")

    try:
        source_repo.delete(source_id)
        flash(content["msg_success"][lang], "success")
        return redirect("/")
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            content["error_common"][lang],
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/delete_tag/<int:source_id>/<string:tag>", methods=["POST"])
def delete_tag(source_id, tag):
    tag_repo = TagRepository(DatabaseService())
    lang = session.get("lang", "fi")

    try:
        tag_repo.delete(source_id, tag)
        flash(content["msg_success"][lang], "success")
        return redirect("/")
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            content["error_common"][lang],
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/tag", methods=["POST"])
def tag_post():
    tag_repo = TagRepository(DatabaseService())
    lang = session.get("lang", "fi")

    form = request.form
    try:
        tag_repo.create(
            Tag(
                {
                    "name": form["name"] if "name" in form else "",
                    "source_id": form["source_id"] if "source_id" in form else "",
                    "tag_id": 0,
                }
            )
        )
        flash(content["msg_success"][lang], "success")
        return redirect("/")
    except UserInputError as error:
        flash(error.lang(lang), "error")
        return redirect("/")
    except Exception as error:  # pylint: disable=broad-exception-caught
        flash(
            str(error),
            "error",
        )
        print(error)
        return redirect("/")


@app.route("/download", methods=["GET"])
def download():
    source_repo = SourceRepository(DatabaseService())
    bibtex_string = to_bibtex(source_repo.get_full())

    # doing it this way instead of creating a proper file
    # means it doesn't have to be stored anywhere
    bibtex_bytes = BytesIO(bibtex_string.encode("utf-8"))

    return send_file(
        bibtex_bytes,
        mimetype="text/bib",
        as_attachment=True,
        download_name="references.bib",
    )


@app.route("/language", methods=["GET"])
def language():
    lang = session.get("lang", "fi")
    lang = "en" if lang == "fi" else "fi"
    session["lang"] = lang

    return redirect("/")


@app.route("/reset_db", methods=["GET"])
def reset_db():
    truncate_db()
    return redirect("/")


@app.route("/source/<int:source_id>", methods=["GET"])
def get_source_details(source_id):
    source_repo = SourceRepository(DatabaseService())
    try:
        source = first_item(source_repo.get_full(source_id))

        if not source:
            return {"error": "Source not found"}, 404

        return source.__dict__, 200

    except Exception as error:  # pylint: disable=broad-exception-caught
        print(error)
        return {"error": "Failed to fetch source details"}, 500


@app.route("/clear_session", methods=["GET"])
def clear_session():
    lang = session.get("lang", "fi")
    session.clear()
    session["lang"] = lang
    return ""
