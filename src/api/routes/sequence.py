from typing import Annotated, List
from fastapi import APIRouter, Depends, status
from fastapi.responses import ORJSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from api.dependencies import get_sequence_service
from service import models
from service.sequence_service import SequenceService

router = APIRouter(prefix="/sequence")

@router.get("/")
def get_sequences(
    sequence_service: Annotated[SequenceService, Depends(get_sequence_service)],
) -> List[models.Sequence]:
    sequences = sequence_service.get_all_sequences()
    return ORJSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(sequences))

@router.get("/{sequence_id}")
def get_sequence(
    sequence_id: int,
    sequence_service: Annotated[SequenceService, Depends(get_sequence_service)],
) -> models.Sequence:
    sequence = sequence_service.get_sequence(id=sequence_id)
    return ORJSONResponse(status_code=status.HTTP_200_OK, content=sequence)

class CreateSequence(BaseModel):
    name: str
    data: str

@router.post("/")
def add_sequence(
    sequence: CreateSequence,
    sequence_service: Annotated[SequenceService, Depends(get_sequence_service)],
) -> int:
    sequence_id = sequence_service.create_sequence(name=sequence.name, data=sequence.data)
    return ORJSONResponse(status_code=status.HTTP_201_CREATED, content=sequence_id)