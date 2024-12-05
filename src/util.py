from typing import Optional, TypeVar


T = TypeVar("T")


class UserInputError(Exception):
    def __init__(self, content_item):
        self.content_item = content_item

    def lang(self, language) -> str:
        return self.content_item[language]


def try_parse_int(string):
    try:
        return int(string)
    except ValueError:
        return None


def first_item(lst: list[T]) -> Optional[T]:
    if len(lst) == 0:
        return None

    return lst[0]
