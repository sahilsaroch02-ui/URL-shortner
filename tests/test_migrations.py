import os
import subprocess
import sys
from pathlib import Path

from sqlalchemy import create_engine, inspect


def test_alembic_upgrade_head_creates_urls_table(tmp_path: Path) -> None:
    database_path = tmp_path / "migration.db"
    database_url = f"sqlite:///{database_path}"
    env = os.environ | {"DATABASE_URL": database_url}

    result = subprocess.run(
        [sys.executable, "-m", "alembic", "upgrade", "head"],
        check=False,
        capture_output=True,
        env=env,
        text=True,
    )

    assert result.returncode == 0, result.stderr

    engine = create_engine(database_url)
    inspector = inspect(engine)

    assert "urls" in inspector.get_table_names()
    columns = {column["name"] for column in inspector.get_columns("urls")}
    assert columns == {
        "id",
        "original_url",
        "short_code",
        "created_at",
        "expires_at",
        "click_count",
        "is_active",
    }
