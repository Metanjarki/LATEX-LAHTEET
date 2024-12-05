from db_util import source_exists_by_id
from util import UserInputError
from content import content, combine


class Tag:
    def __init__(self, data: dict):
        self.source_id = data["source_id"]
        self.name = data["name"]
        self.tag_id = data["tag_id"]

    def validate(self):
        if len(self.name) == 0:
            raise UserInputError(combine(content["name"], content["is_required"]))

        if not source_exists_by_id(self.source_id):
            raise UserInputError(content["error_source_not_found"])
