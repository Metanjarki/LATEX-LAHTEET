import unittest
from entities.inproceedings import Inproceedings
from util import UserInputError

class TestSource(unittest.TestCase):

    def setUp(self):
        self.data = {
        "source_id"     : "1",
        "bibtex_key"    : "key",   
        "title"         : "title",
        "year"          : "2024",
        "author"        : "author",
        "booktitle"     : "booktitle",
        "editor"        : "editor",
        "series"        : "series",
        "pages"         : "pages",
        "address"       : "address",
        "month"         : "month",
        "organization"  : "organization",
        "publisher"     : "publisher",
        "volume"        : "volume",
        "tags"          : "tags",
        }

        self.source = Inproceedings(self.data)
        return super().setUp()
    
    def test_super_validate(self):
        self.source.bibtex_key = []
        with self.assertRaises(UserInputError):
            self.source.validate()
    
    def test_wrong_booktitle(self):
        self.source.booktitle = []
        with self.assertRaises(UserInputError):
            self.source.validate()
    
    def test_no_volume(self):
        self.source.volume = "-1"
        with self.assertRaises(UserInputError):
            self.source.validate()
    