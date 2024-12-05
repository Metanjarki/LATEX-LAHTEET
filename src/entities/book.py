from entities.source import Source
from util import UserInputError


class Book(Source):
    def __init__(self, data: dict):
        super().__init__(data)
        self.source_book_id = data["source_book_id"]
        self.publisher = data["publisher"]
        self.kind = "book"

    def to_dict(self):
        base = super().to_dict()
        base.update({
                "source_id": self.source_id,
                "bibtex_key": self.bibtex_key,
                "title": self.title,
                "year": self.year,
                "author": self.author,
                "publisher": self.publisher,
                "tags": self.tags,
        })
        return base

    def validate(self):
        if len(self.publisher) == 0:
            raise UserInputError("Julkaisija vaaditaan")
        super().validate()