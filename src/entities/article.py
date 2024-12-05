from string import digits

from entities.source import Source
from util import UserInputError
from content import content, combine


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

    def validate(self):
        super().validate()

        if len(self.journal) == 0:
            raise UserInputError(combine(content["journal"], content["is_required"]))

        if len(self.volume) > 0 and not set(self.volume).issubset(set(digits)):
            raise UserInputError(combine(content["volume"], content["must_be_number"]))

        if len(self.number) > 0 and not set(self.number).issubset(set(digits)):
            raise UserInputError(combine(content["number"], content["must_be_number"]))

