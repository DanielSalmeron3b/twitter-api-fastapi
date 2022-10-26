# Python
from enum import Enum
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import (
    BaseModel, EmailStr, Field,
    validator,
    )

# FastAPI
from fastapi import FastAPI

app = FastAPI()

# Models

class Gender(Enum):
    female = "female"
    male = "male"
    other = "other"


class User(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(
        ...,
        min_length=8,
        max_length=16
    )
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    birth_date: Optional[date] = Field(example='2000-01-01')
    gender: Optional[Gender] = Field(default=None, example=Gender.male)

    # birth_date validation, user must be over 14 years old
    @validator('birth_date')
    def is_over_fourteen(cls, user_birth_date):
        current_date = date.today()
        delta = current_date - user_birth_date
        if delta.days <= 14:
            raise ValueError('User must be over 14 years old')
        else:
            return user_birth_date

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}