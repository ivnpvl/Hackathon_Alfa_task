import os
from pydantic_settings import BaseSettings

"""
Базовые классы настроек, по необходимости можно расширять.
DEBUG можно использовать для разнообразной логики, например:
в db/database.py при создании движка - выводить/не выводить запросы в консоль.
"""


class PostgresSettings(BaseSettings):
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = os.getenv("DB_PORT", 5432)
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASS: str = os.getenv("DB_PASS", "postgres")
    DB_NAME: str = os.getenv("DB_NAME", "localhost")

    @property
    def database_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
        )


settings = PostgresSettings()
