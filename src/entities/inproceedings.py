from string import digits

from entities.source import Source
from util import UserInputError
from content import content, combine_language_items


class Inproceedings(Source):
    def __init__(self, data: dict):
        super().__init__(data)
        self.source_inproceedings_id = data["source_inproceedings_id"]
        self.booktitle = data["booktitle"]
        self.editor = data["editor"]
        self.series = data["series"]
        self.pages = data["pages"]
        self.address = data["address"]
        self.month = data["month"]
        self.organization = data["organization"]
        self.publisher = data["publisher"]
        self.volume = data["volume"]
        self.kind = "inproceedings"

    def validate(self):
        super().validate()

        if len(self.booktitle) == 0:
            raise UserInputError(
                combine_language_items(content["booktitle"], content["is_required"])
            )

        if len(self.volume) > 0 and not set(self.volume).issubset(set(digits)):
            raise UserInputError(
                combine_language_items(content["volume"], content["must_be_number"])
            )
