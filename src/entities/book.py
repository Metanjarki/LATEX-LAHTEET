from entities.source import Source
from util import UserInputError
from content import content, combine


class Book(Source):
    def __init__(self, data: dict):
        super().__init__(data)
        self.source_book_id = data["source_book_id"]
        self.publisher = data["publisher"]
        self.kind = "book"

    def validate(self):
        super().validate()
        if len(self.publisher) == 0:
            raise UserInputError(combine(content["publisher"], content["is_required"]))
