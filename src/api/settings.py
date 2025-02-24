from typing import Optional
from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DB(BaseModel):
    url: Optional[str] = None
    username: Optional[str] = None
    password: Optional[SecretStr] = None
    
    pool_size: Optional[int] = 5

class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(frozen=True, extra="ignore", env_nested_delimiter="_")

    DB: DB