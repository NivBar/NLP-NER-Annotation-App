from enum import Enum, auto
from typing import List
from uuid import UUID

from pydantic import BaseModel


class InputItem(BaseModel):
    ID: str
    text: str


class NERLabel(Enum):
    NONE = auto()
    PERSON = auto()
    LOCATION = auto()
    DEVICE = auto()
    COUNTRY = auto()
    COMPANY = auto()
    OTHER = auto()


class WordStructure(BaseModel):
    word: str
    label: List[NERLabel] = [NERLabel.NONE]
    position: int
    sentence_id: str


class OutputItem(BaseModel):
    ID: UUID
    labeled_data: List[WordStructure]
