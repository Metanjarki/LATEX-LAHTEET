from pathlib import Path

from sqlalchemy import text

from config import db, app


def setup_db():
    # Luo uusi skeema tiedoston /src/schema.sql pohjalta
    path = Path(__file__).parent / "../schema.sql"
    with path.open() as fp:
        sql = fp.read()
        db.session.execute(text(sql))

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
