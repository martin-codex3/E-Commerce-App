from pydantic_settings import SettingsConfigDict, BaseSettings


# we will attempt to get the environment settings here
class AppConfig(BaseSettings):
    DATABASE_URL: str

    # using the settings dict here
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


# we will create the object for the config class here
app_config = AppConfig()