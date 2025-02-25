from typing import List, Set
from service import models
from service.repository import SequenceRepository


class SequenceService:
    def __init__(self, sequence_repository: SequenceRepository):
        self.sequence_repository = sequence_repository
    
    def get_sequence(self, id: int) -> models.Sequence:
        return self.sequence_repository.get(sequence_id=id)
    
    def get_multiple_sequences(self, ids: Set[int]) -> List[models.Sequence]:
        return self.sequence_repository.getmany(sequence_ids=ids)
    
    def get_all_sequences(self) -> List[models.Sequence]:
        return self.sequence_repository.getall()
    
    def create_sequence(self, name: str, data: str) -> int:
        return self.sequence_repository.add(name=name, data=data)