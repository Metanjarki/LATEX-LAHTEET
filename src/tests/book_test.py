import unittest
from entities.book import Book
from util import UserInputError

class TestSource(unittest.TestCase):

    def setUp(self):
        self.data = {
        "source_book_id": "1",
        "source_id"     : "1",
        "bibtex_key"    : "key",   
        "title"         : "title",
        "year"          : "2024",
        "author"        : "author",
        "publisher"     : "publisher",
        "tags"          : "tags",
        }
        self.test_data = {
        "source_id"     : "1",
        "bibtex_key"    : "key",   
        "title"         : "title",
        "year"          : "2024",
        "author"        : "author",
        "publisher"     : "publisher",
        "tags"          : "tags",
        }
        self.source = Book(self.data)
        return super().setUp()
    
    def test_super_validate(self):
        self.source.bibtex_key = []
        with self.assertRaises(UserInputError):
            self.source.validate()
    
    def test_wrong_publisher(self):
        self.source.publisher = []
        with self.assertRaises(UserInputError):
            self.source.validate()