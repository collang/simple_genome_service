from functools import lru_cache
from typing import Annotated, Generator
from fastapi import Depends
from sqlalchemy import Connection, Engine, create_engine

from api.settings import ApiSettings
from service.repository import SequenceRepository
from service.sequence_service import SequenceService


def get_api_settings() -> ApiSettings:
    return ApiSettings()

@lru_cache(maxsize=1) # DB Engine will be a singleton as long as settings do not change
def get_db_engine(api_settings: Annotated[ApiSettings, Depends(get_api_settings)]) -> Engine:
    return create_engine("sqlite+pysqlite:///:memory:", echo=True)

def get_db_connection(db_engine: Annotated[Engine, Depends(get_db_engine)]) -> Generator[Connection, None, None]:
    with db_engine.connect() as connection:
        yield connection

def get_sequence_repository(
    connection: Annotated[Connection, Depends(get_db_connection)]
) -> SequenceRepository:
    return SequenceRepository(connection=connection)

def get_sequence_service(
    sequence_repostitory: Annotated[SequenceRepository, Depends(get_sequence_repository)]
) -> SequenceService:
    return SequenceService(sequence_repository=sequence_repostitory)