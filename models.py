# Python
from enum import Enum
from uuid import UUID
from datetime import (
    date, datetime
    )
from typing import Optional

# Pydantic
from pydantic import (
    BaseModel, EmailStr, Field,
    validator,
    )

# Models

class Gender(Enum):
    female = "female"
    male = "male"
    other = "other"

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class PasswordMixin(BaseModel):
        password: str = Field(
        ...,
        min_length=8,
        max_length=16,
        example="password123",
    )

class User(UserBase):
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

class UserRegister(User, PasswordMixin):
    pass

class UserLogin(PasswordMixin, UserBase):
    pass


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256,
    )
    created_at: datetime = Field(default=datetime.utcnow(),)
    update_at: Optional[datetime] = Field()
    by: User = Field(...)