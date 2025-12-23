from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):

    DATABASE_URL: str
    JWT_ALGORITHM: str
    JWT_KEY: str
    ALLOWED_ORIGIN_ONE: str
    ALLOWED_ORIGIN_TWO: str
    ALLOWED_ORIGIN_THREE: str

    model_config = SettingsConfigDict(
        env_file=".env",
    )


# creating the object for the settings
AppConfig = AppConfig()
