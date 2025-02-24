from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from api.dependencies import get_genome_repository
from service.repository import GenomeRepository

router = APIRouter(prefix="/sequence")

@router.get("/")
def get_sequences(
    genome_repository: Annotated[GenomeRepository, Depends(get_genome_repository)],
):
    return genome_repository.getall()

@router.get("/{sequence_id}")
def get_sequence(
    sequence_id: int,
    genome_repository: Annotated[GenomeRepository, Depends(get_genome_repository)],
):
    return genome_repository.get(sequence_id=sequence_id)


class CreateSequence(BaseModel):
    name: str
    data: str

class Sequence(BaseModel):
    id: int
    name: str
    data: str

@router.post("/")
def add_sequence(
    sequence: CreateSequence,
    genome_repository: Annotated[GenomeRepository, Depends(get_genome_repository)],
):
    return genome_repository.add(name=sequence.name, data=sequence.data)