from enum import Enum
from typing import Self

from pydantic import HttpUrl, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict

class Browsers(str, Enum):
    CHROMIUM = "chromium"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    base_url: HttpUrl
    headless: bool
    browsers: list[Browsers]
    login_username: str | None = None
    login_password: str | None = None
    reports: DirectoryPath

    @classmethod
    def initialize(cls) -> Self:
        reports_dir = DirectoryPath("./reports")
        reports_dir.mkdir(exist_ok=True)

        return Settings(
            reports=reports_dir
        )


settings = Settings.initialize()
