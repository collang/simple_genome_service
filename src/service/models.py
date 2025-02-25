from typing import Optional
from pydantic import BaseModel

class Sequence(BaseModel):
    id: Optional[int] = None
    name: str
    data: str
