from pydantic_settings import SettingsConfigDict, BaseSettings


class ProjectConfig(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
    )



# we will create an object for the class here
ProjectConfig = ProjectConfig()
