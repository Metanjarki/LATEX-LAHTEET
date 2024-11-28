from string import digits

from entities.source import Source
from util import UserInputError


class Inproceedings(Source): #pylint: disable=too-few-public-methods,too-many-instance-attributes
    def __init__( #pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals
        self,
        source_id,
        bibtex_key,
        title,
        year,
        author,
        source_inproceedings_id,
        booktitle,
        editor,
        series,
        pages,
        address,
        month,
        organization,
        publisher,
        volume,
    ):
        super().__init__(source_id, bibtex_key, title, year, author)
        self.source_inproceedings_id = source_inproceedings_id
        self.booktitle = booktitle
        self.editor = editor
        self.series = series
        self.pages = pages
        self.address = address
        self.month = month
        self.organization = organization
        self.publisher = publisher
        self.volume = volume

    def validate(self):
        super().validate()

        if len(self.booktitle) == 0:
            raise UserInputError("Kirjan otsikko vaaditaan")

        if len(self.volume) > 0 and not set(self.volume).issubset(set(digits)):
            raise UserInputError("Kentän nide on oltava numero")
