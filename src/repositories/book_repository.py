from config import db, schema_name
from sqlalchemy import text

from entities.book import Book


class BookRepository:
    @staticmethod
    def get():
        sql = f"""
            SELECT
                s.source_id,
                s.bibtex_key,
                s.title,
                s.year,
                s.author,
                sb.source_book_id,
                sb.publisher

            FROM {schema_name}.source_book sb

            LEFT JOIN {schema_name}.source s
            ON s.source_id = sb.source_id
        """
        result = db.session.execute(text(sql))
        books = result.fetchall()

        # NOTE: Varmista että SELECT queryn palattamat kentät ovat samat kuin olion konstruktorin,
        #  muutoin laita kentät manuaalisesti tyyliin SourceBook(book[0], book[1], jne...)

        # * -operaattori "avaa" listan, esim ["a", "b", "c"] --> "a", "b", "c"
        return [Book(*book) for book in books]

    @staticmethod
    def create(book):
        book.validate()

        # Tapa lisätä useihin tauluihin siten, että pääsemme kätevästi
        #  käsiksi edellisen lisäyksen ID:hen
        sql = f"""
            WITH q AS (
                INSERT INTO {schema_name}.source
                (title, year, bibtex_key, kind, author) 
                VALUES
                (:title, :year, :bibtex_key, 'book', :author)
                RETURNING source_id
            )
            INSERT INTO {schema_name}.source_book
                (source_id, publisher)
                VALUES
                ((SELECT source_id FROM q), :publisher)

        """
        db.session.execute(
            text(sql),
            {
                "bibtex_key": book.bibtex_key,
                "title": book.title,
                "year": book.year,
                "publisher": book.publisher,
                "author": book.author,
            },
        )
        db.session.commit()