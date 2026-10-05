from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://hanbitai:hanbitai@localhost:5432/hanbitai"
    jwt_secret: str = "dev-secret-change-me"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60
    admin_email: str = "admin@hanbitai.com"
    admin_password: str = "change-this-password"
    cors_origins: str = "http://localhost:4200"


settings = Settings()
