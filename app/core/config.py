from dataclasses import dataclass
from functools import lru_cache
from os import getenv


@dataclass(frozen=True)
class Settings:
    app_name: str = "URL Shortener"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = False
    database_url: str = "sqlite:///./url_shortener.db"
    short_code_length: int = 7
    default_expiration_days: int = 30

    def __post_init__(self) -> None:
        if self.short_code_length < 4 or self.short_code_length > 10:
            raise ValueError("SHORT_CODE_LENGTH must be between 4 and 10")
        if self.default_expiration_days < 1:
            raise ValueError("DEFAULT_EXPIRATION_DAYS must be greater than 0")
        if not self.database_url:
            raise ValueError("DATABASE_URL must not be empty")


def _env_bool(name: str, default: bool) -> bool:
    value = getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _env_int(name: str, default: int) -> int:
    value = getenv(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer") from exc


@lru_cache
def get_settings() -> Settings:
    return Settings(
        app_name=getenv("APP_NAME", Settings.app_name),
        app_version=getenv("APP_VERSION", Settings.app_version),
        environment=getenv("ENVIRONMENT", Settings.environment),
        debug=_env_bool("DEBUG", Settings.debug),
        database_url=getenv("DATABASE_URL", Settings.database_url),
        short_code_length=_env_int("SHORT_CODE_LENGTH", Settings.short_code_length),
        default_expiration_days=_env_int(
            "DEFAULT_EXPIRATION_DAYS",
            Settings.default_expiration_days,
        ),
    )
