from pydantic import BaseModel
from pydantic.config import ConfigDict
from typing import Generic, TypeVar, List, Optional

# --- QUESTION SCHEMAS ---
class SQuestionNoID(BaseModel):
    question: str
    answer: str
    topic_id: int

class SQuestion(SQuestionNoID):
    id: int
    # question: str
    # answer: str
    # topic_id: int | None = None
    model_config = ConfigDict(from_attributes=True)

# --- TOPIC SCHEMAS ---
class STopicNoID(BaseModel):
    name: str
    parent_id: int | None = None

class STopic(STopicNoID):
    id: int
    # name: str
    # parent_id: int | None = None
    
    model_config = ConfigDict(from_attributes=True)

class STopicTree(BaseModel):
    id: int
    name: str
    children: List['STopicTree']
    questions: List['SQuestion']

# --- RESPONSE SCHEMAS ---
T = TypeVar("T")

class SResponse(BaseModel, Generic[T]):
    message: str
    code: int
    data: T | None = None

class SChildren(BaseModel):
    parent_topic: str
    topics: list[STopic]
    questions: list[SQuestion]







