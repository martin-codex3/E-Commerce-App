from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
    )


# creating the object for the settings
AppConfig = AppConfig()
