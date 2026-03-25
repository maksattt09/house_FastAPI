from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from .models import StatusChoices, LanguageChoices, PropertyChoices, ConditionChoices
from datetime import datetime



class HouseSchema(BaseModel):
    GrLivArea: int
    YearBuilt: int
    GarageCars: int
    TotalBsmtSF: int
    FullBath: int
    OverallQual: int
    Neighborhood: str


class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    age: Optional[int]
    phone_number: Optional[str]
    role: Optional[StatusChoices]
    preferred_language: Optional[LanguageChoices]



class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    age: Optional[int]
    phone_number: Optional[str]
    role: StatusChoices
    preferred_language: LanguageChoices

    model_config = ConfigDict(from_attributes=True)


class PropertyInputSchema(BaseModel):
    tittle: str
    description: Optional[str]
    property_type: Optional[PropertyChoices]
    region: str
    city: str
    district: str
    address: str
    area: str
    price: int
    rooms: int
    floor: int
    total_floors: int
    condition: Optional[ConditionChoices]
    images: Optional[str]
    documents: str
    seller_id: int


class PropertyOutSchema(BaseModel):
    id: int
    tittle: str
    property_type: Optional[PropertyChoices] = None
    condition: Optional[ConditionChoices] = None
    region: str
    city: str
    district: str
    address: str
    area: str
    price: int
    rooms: int
    floor: int
    total_floors: int
    created_date: datetime
    condition: ConditionChoices
    images: Optional[str]
    documents: str
    seller_id: int

    model_config = ConfigDict(from_attributes=True)


class ReviewInputSchema(BaseModel):
    author_id: int
    seller_rev_id: int
    rating: int
    comment: str


class ReviewOutSchema(BaseModel):
    id: int
    author_id: int
    seller_rev_id: int
    rating: int
    comment: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserLoginSchema(BaseModel):
    username: str
    password: str
