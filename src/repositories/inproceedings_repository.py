from typing import Optional

from config import SCHEMA_NAME
from entities.inproceedings import Inproceedings
from util import try_parse_int
import repositories.source_repository


class InproceedingsRepository:

    def __init__(self, database_service) -> None:
        self.database_service = database_service

    def get(self, source_id: Optional[int] = None) -> list[Inproceedings]:
        sql = f"""
            SELECT
                s.source_id,
                s.bibtex_key,
                s.title,
                s.year,
                s.author,
                si.source_inproceedings_id,
                si.booktitle,
                si.editor,
                si.series,
                si.pages,
                si.address,
                si.month,
                si.organization,
                si.publisher,
                si.volume

            FROM {SCHEMA_NAME}.source_inproceedings si

            LEFT JOIN {SCHEMA_NAME}.source s
            ON s.source_id = si.source_id

            {f"WHERE s.source_id = '{source_id}'" if source_id else ""}
        """
        rows = self.database_service.fetch(sql)

        return [Inproceedings(row) for row in rows]

    def create(self, inproceedings):
        inproceedings.validate()

        # Tapa lisätä useihin tauluihin siten, että pääsemme kätevästi
        #  käsiksi edellisen lisäyksen ID:hen
        sql = f"""
            WITH q AS (
                INSERT INTO {SCHEMA_NAME}.source
                (title, year, bibtex_key, kind, author) 
                VALUES
                (:title, :year, :bibtex_key, 'inproceedings', :author)
                RETURNING source_id
            )
            INSERT INTO {SCHEMA_NAME}.source_inproceedings
                (source_id, booktitle, editor, series, pages, address, month, organization, publisher, volume)
                VALUES
                ((SELECT source_id FROM q), :booktitle, :editor, :series, :pages, :address, :month, :organization, :publisher, :volume)
        """

        self.database_service.execute(
            sql,
            {
                "bibtex_key": inproceedings.bibtex_key,
                "title": inproceedings.title,
                "year": inproceedings.year,
                "author": inproceedings.author,
                "booktitle": inproceedings.booktitle,
                "editor": inproceedings.editor,
                "series": inproceedings.series,
                "pages": inproceedings.pages,
                "address": inproceedings.address,
                "month": inproceedings.month,
                "organization": inproceedings.organization,
                "publisher": inproceedings.publisher,
                "volume": try_parse_int(inproceedings.volume),
            },
        )

    def update(self, inproceedings):
        inproceedings.validate()
        repositories.source_repository.SourceRepository(self.database_service).update(
            inproceedings
        )

        sql = f"""
            UPDATE {SCHEMA_NAME}.source_inproceedings SET
            booktitle = :booktitle,
            editor = :editor,
            series = :series,
            pages = :pages,
            address = :address,
            month = :month,
            organization = :organization,
            publisher = :publisher,
            volume = :volume

            WHERE source_id = :source_id
        """
        self.database_service.execute(
            sql,
            {
                "booktitle": inproceedings.booktitle,
                "editor": inproceedings.editor,
                "series": inproceedings.series,
                "pages": inproceedings.pages,
                "address": inproceedings.address,
                "month": inproceedings.month,
                "organization": inproceedings.organization,
                "publisher": inproceedings.publisher,
                "volume": try_parse_int(inproceedings.volume),
                "source_id": inproceedings.source_id,
            },
        )
