import pytest

from app.core.config import Settings, get_settings
from app.main import create_app


def test_settings_use_safe_defaults() -> None:
    settings = Settings()

    assert settings.app_name == "URL Shortener"
    assert settings.environment == "development"
    assert settings.database_url == "sqlite:///./url_shortener.db"
    assert settings.short_code_length == 7
    assert settings.default_expiration_days == 30


def test_settings_load_environment_overrides(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_NAME", "Test Shortener")
    monkeypatch.setenv("APP_VERSION", "1.2.3")
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("DEBUG", "true")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/urls")
    monkeypatch.setenv("SHORT_CODE_LENGTH", "9")
    monkeypatch.setenv("DEFAULT_EXPIRATION_DAYS", "14")
    get_settings.cache_clear()

    settings = get_settings()

    assert settings.app_name == "Test Shortener"
    assert settings.app_version == "1.2.3"
    assert settings.environment == "test"
    assert settings.debug is True
    assert settings.database_url == "postgresql://user:pass@localhost:5432/urls"
    assert settings.short_code_length == 9
    assert settings.default_expiration_days == 14

    get_settings.cache_clear()


def test_settings_reject_invalid_short_code_length() -> None:
    with pytest.raises(ValueError, match="SHORT_CODE_LENGTH"):
        Settings(short_code_length=3)


def test_create_app_uses_settings_metadata() -> None:
    app = create_app(Settings(app_name="Configured API", app_version="2.0.0"))

    assert app.title == "Configured API"
    assert app.version == "2.0.0"
