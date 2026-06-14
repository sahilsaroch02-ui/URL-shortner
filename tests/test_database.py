from sqlalchemy import text
from sqlalchemy.orm import Session, sessionmaker

from app.core import database
from app.core.database import Base, create_database_engine, get_db


def test_create_database_engine_supports_sqlite_memory() -> None:
    engine = create_database_engine("sqlite:///:memory:")

    with engine.connect() as connection:
        value = connection.execute(text("select 1")).scalar_one()

    assert value == 1


def test_database_base_metadata_starts_empty_before_models() -> None:
    assert Base.metadata.tables == {}


def test_get_db_yields_session(monkeypatch) -> None:
    engine = create_database_engine("sqlite:///:memory:")
    session_factory = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
        class_=Session,
    )
    monkeypatch.setattr(database, "SessionLocal", session_factory)

    dependency = get_db()
    session = next(dependency)

    assert session.execute(text("select 1")).scalar_one() == 1

    try:
        next(dependency)
    except StopIteration:
        pass
