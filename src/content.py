content = {
    "bibtex_key": {"fi": "Avain", "en": "Key"},
    "title": {"fi": "Otsikko", "en": "Title"},
    "year": {"fi": "Julkaisuvuosi", "en": "Year"},
    "author": {"fi": "Kirjoittaja", "en": "Author"},
    "publisher": {"fi": "Julkaisija", "en": "Publisher"},
    "journal": {"fi": "Julkaisu", "en": "Journal"},
    "volume": {"fi": "Nide", "en": "Volume"},
    "number": {"fi": "Numero", "en": "Number"},
    "pages": {"fi": "Sivut", "en": "Pages"},
    "month": {"fi": "Kuukausi", "en": "Month"},
    "booktitle": {"fi": "Kirjan otsikko", "en": "Booktitle"},
    "editor": {"fi": "Editori", "en": "Editor"},
    "series": {"fi": "Sarja", "en": "Series"},
    "address": {"fi": "Osoite", "en": "Address"},
    "organization": {"fi": "Organisaatio", "en": "Organization"},
    "source_info": {"fi": "Lähteen tiedot", "en": "Source details"},
    "add_source": {"fi": "Lisää lähde", "en": "Add source"},
    "add_tag": {"fi": "Lisää tunniste", "en": "Add tag"},
    "filter": {"fi": "Suodata", "en": "Filter"},
    "tag": {"fi": "Tunniste", "en": "Tag"},
    "add": {"fi": "Lisää", "en": "Add"},
    "add_source": {"en": "Add source", "fi": "Lisää lähde"},
    "download_sources": {"en": "Download", "fi": "Lataa lähteet"},
    "name": {"fi": "Nimi", "en": "Name"},
    "page_title": {
        "fi": "BibTex -lähdehallintatyökalu",
        "en": "BibTex source management",
    },
    "article": {
        "fi": "Artikkeli",
        "en": "Article",
    },
    "book": {
        "fi": "Kirja",
        "en": "Book",
    },
    "inproceedings": {
        "fi": "Artikkeli konferenssijulkaisussa",
        "en": "Inproceedings",
    },
    "error_source_not_found": {
        "fi": "Lähdettä ei ole olemassa",
        "en": "Source not found",
    },
    "error_common": {
        "fi": "Toiminto epäonnistui teknisen virheen takia",
        "en": "The action failed due to a technical error",
    },
    "error_key_in_use": {
        "fi": "Avain on jo käytössä",
        "en": "Key is already in use",
    },
    "is_required": {
        "fi": " vaaditaan",
        "en": " is required",
    },
    "error_not_supported": {
        "fi": "Toimintoa ei tueta",
        "en": "This action is not supported",
    },
    "msg_success": {
        "fi": "Toiminto suoritettu onnistuneesti",
        "en": "Action completed successfully",
    },
    "must_be_number": {
        "fi": " on oltava numero",
        "en": " must be a number",
    },
    "error_invalid_bibtex_format": {
        "fi": "Avain saa sisältää vain merkkejä 0-9, a-z, A-Z, -, _ ja :",
        "en": "Key can only contain characters 0-9, a-z, A-Z, -, _ and :",
    },
}


def combine_language_items(item_a, item_b):
    return {
        "fi": item_a["fi"] + item_b["fi"],
        "en": item_a["en"] + item_b["en"],
    }
