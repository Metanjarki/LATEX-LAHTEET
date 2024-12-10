import unittest
from entities.article import Article
from util import UserInputError

class TestSource(unittest.TestCase):

    def setUp(self):
        self.data = {
        "source_article_id" : "1",
        "source_id"         : "1",
        "bibtex_key"        : "key",   
        "title"             : "title",
        "year"              : "2024",
        "author"            : "author",
        "journal"           : "booktitle",
        "pages"             : "pages",
        "month"             : "month",
        "number"            : "organization",
        "volume"            : "volume",
        "tags"              : "tags",
        }

        self.source = Article(self.data)
        return super().setUp()
    
    def test_super_validate(self):
        self.source.bibtex_key = []
        with self.assertRaises(UserInputError):
            self.source.validate()
    
    def test_no_journal(self):
        self.source.journal = []
        with self.assertRaises(UserInputError):
            self.source.validate()
    
    def test_wrong_volume(self):
        self.source.volume = "-1"
        with self.assertRaises(UserInputError):
            self.source.validate()
    
    def test_wrong_number(self):
        self.source.number = "-1"
        with self.assertRaises(UserInputError):
            self.source.validate()
    