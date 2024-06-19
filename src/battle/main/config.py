from functools import lru_cache
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    """
    The settings class for the bot.
    """

    # The token of the bot.
    token: str


class PostgresSettings(BaseSettings):
    """
    The settings class for the postgres database.
    """

    # The DSN of the postgres database.
    dsn: PostgresDsn


class RedisSettings(BaseSettings):
    """
    The settings class for the redis database.
    """

    # The DSN of the redis database.
    dsn: str


class Settings(BaseSettings):
    """
    The settings class for the application.
    """

    # The environment file to load the settings from.
    model_config = SettingsConfigDict(
        env_file=".env", env_nested_delimiter="__"
    )

    # The name of the application.
    app_name: str = "RPG Game"

    # The version of the application.
    version: str = "0.1.0"

    # The description of the application.
    description: str = "A simple RPG game."

    # The environment the application is running in.
    env: str = "development"

    # The logging settings
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_date_format: str = "%Y-%m-%d %H:%M:%S"
    log_file: str = "rpg_game.log"

    # Bot settings
    bot: BotSettings

    # Postgres DSN
    postgres: PostgresSettings

    # Redis settings
    redis: RedisSettings


@lru_cache
def get_settings() -> Settings:
    """
    Get the settings.
    """
    return Settings()
