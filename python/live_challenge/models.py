from typing import Any

from pydantic import BaseModel, Field


class GenericRequest(BaseModel):
    """Generic payload accepted by the exercise endpoint."""

    data: dict[str, Any] = Field(default_factory=dict)


class GenericResponse(BaseModel):
    id: int
    data: dict[str, Any]


class HealthResponse(BaseModel):
    status: str


class AnswerRequest(BaseModel):
    question: str = Field(min_length=1)
    context: list[str] = Field(min_length=3, max_length=3)


class StructuredAnswer(BaseModel):
    answer: str
    key_points: list[str]
    based_on_context: bool
