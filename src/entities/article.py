from string import digits

from entities.source import Source
from util import UserInputError


class Article(Source):
    def __init__(self, data: dict):
        super().__init__(data)
        self.source_article_id = data["source_article_id"]
        self.journal = data["journal"]
        self.volume = data["volume"]
        self.number = data["number"]
        self.pages = data["pages"]
        self.month = data["month"]
        self.kind = "article"

    def to_dict(self):
        base = super().to_dict()
        base.update(
            {
                "source_id": self.source_id,
                "bibtex_key": self.bibtex_key,
                "title": self.title,
                "year": self.year,
                "author": self.author,
                "journal": self.journal,
                "volume": self.volume,
                "number": self.number,
                "pages": self.pages,
                "month": self.month,
                "tags": self.tags,
            }
        )
        return base

    def validate(self):
        

        if len(self.journal) == 0:
            raise UserInputError("Julkaisu vaaditaan")

        if len(self.volume) > 0 and not set(self.volume).issubset(set(digits)):
            raise UserInputError("Kentän nide on oltava numero")

        if len(self.number) > 0 and not set(self.number).issubset(set(digits)):
            raise UserInputError("Kentän numero on oltava numero")
        super().validate()