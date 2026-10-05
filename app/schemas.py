from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field

Service = Literal[
    "AI Agent Creation",
    "AI Course",
    "Website Development",
    "Mobile App Development",
    "Custom AI Solution",
]


class EnquiryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    phone: str | None = Field(default=None, max_length=40)
    service: Service
    budget: str | None = Field(default=None, max_length=60)
    message: str = Field(min_length=10, max_length=4000)


class EnquiryOut(EnquiryCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime


class TestimonialOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    role: str
    company: str
    quote: str
    rating: int
    image_url: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
