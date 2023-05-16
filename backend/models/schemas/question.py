import datetime as dt

from pydantic import Field

from .base import BaseSchemaModel


__all__ = [
    "QuestionInCreateSchema",
    "QuestionOutResponse",
    "QuestionInRequest"
]


class QuestionInRequest(BaseSchemaModel):
    questions_num: int


class QuestionInCreateSchema(BaseSchemaModel):
    question_id: int = Field(..., alias="id")
    text: str = Field(..., alias="question")
    answer: str = Field(..., alias="answer")


class QuestionOutResponse(BaseSchemaModel):
    id: int
    question_id: int
    text: str
    answer: str
    created_at: dt.datetime
    updated_at: dt.datetime
