import re

from content import combine_language_items, content
from util import UserInputError


class Source:
    def __init__(self, data: dict):
        self.source_id = data["source_id"]
        self.bibtex_key = data["bibtex_key"]
        self.title = data["title"]
        self.year = data["year"]
        self.author = data["author"]

        self.tags = []
        if "tags" in data and data["tags"]:
            self.tags = data["tags"].split(",")

        self.kind = "misc"
        self.stringify_ignore_fields = [
            "kind",
            "stringify_ignore_fields",
            "bibtex_key",
            "tags",
        ]

    def validate(self):
        if not re.compile("^[0-9a-zA-Z\\-_:]*$").match(str(self.bibtex_key)):
            raise UserInputError(content["error_invalid_bibtex_format"])

        if len(self.title) == 0:
            raise UserInputError(
                combine_language_items(content["title"], content["is_required"])
            )

        if len(self.author) == 0:
            raise UserInputError(
                combine_language_items(content["author"], content["is_required"])
            )

        if len(self.year) == 0:
            raise UserInputError(
                combine_language_items(content["year"], content["is_required"])
            )

        if not re.compile("^[0-9]+$").match(self.year):
            raise UserInputError(
                combine_language_items(content["year"], content["must_be_number"])
            )

    # str(objekti) muuntaa sen bibtex-muotoon
    def __str__(self) -> str:
        fields = self.__dict__
        fields_bibtex = ""

        for field, value in fields.items():
            if field in self.stringify_ignore_fields:
                continue

            if field.endswith("_id"):
                continue

            if len(str(value)) == 0:
                continue

            value = "{" + str(value) + "}"
            fields_bibtex += f"    {field} = {value},\n"

        return f"@{self.kind}" + "{" + f"{self.bibtex_key},\n{fields_bibtex}" + "}"
