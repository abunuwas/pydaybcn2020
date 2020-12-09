# generated by datamodel-codegen:
#   filename:  oas.yaml
#   timestamp: 2020-12-08T16:09:12+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Status(Enum):
    pending = 'pending'
    progress = 'progress'
    completed = 'completed'


class CreateTaskSchema(BaseModel):
    status: Optional[Status] = 'pending'
    task: str


class Status1(Enum):
    pending = 'pending'
    progress = 'progress'
    completed = 'completed'


class GetTaskSchema(BaseModel):
    id: UUID
    created: int = Field(..., description='Date in the form of UNIX timestmap')
    status: Status1
    task: str
