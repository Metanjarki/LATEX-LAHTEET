import json


class FormField:  # pylint: disable=too-few-public-methods
    def __init__(self, name, required=False, input_type="text"):
        self.name = name
        self.required = required
        self.input_type = input_type


# Lomake luodaan tämän muuttujan perusteella
# "common" -listan kentät ovat kaikissa viitetyypeissä
fields = {
    "common": [
        FormField("bibtex_key", True),
        FormField("title", True),
        FormField("year", True),
    ],
    "book": [
        FormField("author", True),
        FormField("publisher", True),
    ],
    "article": [
        FormField("author", True),
        FormField("journal", True),
        FormField("volume", False, "number"),
        FormField("number", False, "number"),
        FormField("pages"),
        FormField("month"),
    ],
    "inproceedings": [
        FormField("author", True),
        FormField("booktitle", True),
        FormField("editor"),
        FormField("series"),
        FormField("pages"),
        FormField("address"),
        FormField("month"),
        FormField("organization"),
        FormField("publisher"),
        FormField("volume", False, "number"),
    ],
}


def get_fields_json():
    serializeable = {key: [f.__dict__ for f in value] for key, value in fields.items()}
    return json.dumps(serializeable)
