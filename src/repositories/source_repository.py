from typing import Optional

from util import first_item
from config import SCHEMA_NAME
from entities.source import Source
import repositories.article_repository
import repositories.book_repository
import repositories.inproceedings_repository


class SourceRepository:

    def __init__(self, database_service) -> None:
        self.database_service = database_service

    def get(self, source_id: Optional[int] = None) -> list[Source]:
        sql = f"""
            SELECT
                s.source_id,
                s.bibtex_key,
                s.title,
                s.year,
                s.author,
                STRING_AGG(t.name, ',') AS tags

            FROM {SCHEMA_NAME}.source s

            LEFT JOIN {SCHEMA_NAME}.tag t
            ON t.source_id = s.source_id

            {f"WHERE s.source_id = '{source_id}'" if source_id else ""}

            GROUP BY s.source_id
            ORDER BY s.source_id
        """
        rows = self.database_service.fetch(sql)

        return [Source(row) for row in rows]

    def delete(self, source_id):
        sql = f"""
            DELETE FROM
            {SCHEMA_NAME}.source
            WHERE source_id = :source_id
        """
        self.database_service.execute(sql, {"source_id": source_id})

    def get_full(self, source_id: Optional[int] = None):
        # Hakee lähteet ns. itsenään, eli esim. kirjalähteistä
        #  haetaan Book objektit kaiken datan kera jne.

        sql = f"""
            SELECT source_id, kind FROM {SCHEMA_NAME}.source
            {f"WHERE source_id = '{source_id}'" if source_id else ""}
        """
        rows = self.database_service.fetch(sql)

        return [
            self.__get_full_information(row["kind"], row["source_id"]) for row in rows
        ]

    def __get_full_information(self, kind, source_id):
        match kind:
            case "book":
                return first_item(
                    repositories.book_repository.BookRepository(
                        self.database_service
                    ).get(source_id)
                )
            case "article":
                return first_item(
                    repositories.article_repository.ArticleRepository(
                        self.database_service
                    ).get(source_id)
                )
            case "inproceedings":
                return first_item(
                    repositories.inproceedings_repository.InproceedingsRepository(
                        self.database_service
                    ).get(source_id)
                )
            case "misc":
                return first_item(self.get(source_id))
            case _:
                raise NotImplementedError

    def update(self, source):
        source.validate()

        sql = f"""
                UPDATE {SCHEMA_NAME}.source SET

                title = :title,
                year = :year,
                author = :author

                WHERE source_id = :source_id


        """
        self.database_service.execute(
            sql,
            {
                "source_id": source.source_id,
                "title": source.title,
                "year": source.year,
                "author": source.author,
            },
        )
