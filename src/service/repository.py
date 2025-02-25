from typing import List, Set
from sqlalchemy import Connection, text

from src.service.database import tables
from src.service import models

class SequenceRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

        self.add_statement = text("INSERT INTO sequence (name, data) VALUES (:name, :data);")
        self.get_statement = text("SELECT * FROM sequence WHERE sequence.id = :sequence_id;")
        self.getall_statement = text("SELECT id FROM sequence;")
    
    def add(self, name: str, data: str):
        return self._add(name=name, data=data)
    
    def get(self, sequence_id: int):
        return self._get(sequence_id)
    
    def getmany(self, sequence_ids: Set[int]):
        return self._getmany(sequence_ids)
    
    def getall(self):
        return self._getall()

    def _add(self, name: str, data: str) -> int:
        with self.connection.begin():
            result = self.connection.execute(
                tables.sequence.insert().values(name=name, data=data)
            )
            self.connection.commit()
            return result.inserted_primary_key[0]

    def _get(self, sequence_id: int) -> models.Sequence:
        with self.connection.begin():
            result = self.connection.execute(
                tables.sequence.select().where(tables.sequence.c.id == sequence_id)
            )
            self.connection.commit()
            models.Sequence.model_validate(obj=result.mappings().fetchone())
    
    def _getmany(self, sequence_ids: Set[int]) -> List[models.Sequence]:
        """Get many sequences from the database.
        
        TODO: Add pagination and sorting.
        """
        with self.connection.begin():
            results = self.connection.execute(
                tables.sequence.select().where(tables.sequence.c.id.in_(sequence_ids))
            )
            self.connection.commit()
            return [models.Sequence.model_validate(result) for result in results.mappings().fetchall()]
    
    def _getall(self) -> List[models.Sequence]:
        """Get all sequences from database.
        
        TODO: Add pagination and sorting
        """
        with self.connection.begin():
            results = self.connection.execute(tables.sequence.select())
            self.connection.commit()
            return [models.Sequence.model_validate(result) for result in results.mappings().fetchall()]