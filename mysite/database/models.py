from mysite.database.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, Date, DateTime, ForeignKey, Text, Boolean
from typing import Optional, List
from enum import Enum as PyEnum
from datetime import date, datetime

class StatusChoices(str, PyEnum):
    admin = "admin"
    seller = "seller"
    buyer = "buyer"


class LanguageChoices(str, PyEnum):
    ru = "ru"
    en = "en"
    ky = "ky"


class PropertyChoices(str, PyEnum):
    house = "house"
    apartment = "apartment"
    land = "land"


class ConditionChoices(str, PyEnum):
    new = "new"
    good = "good"
    needs_repair = "needs_repair"


class UserProfile(Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    role: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), default=StatusChoices.buyer)
    preferred_language: Mapped[LanguageChoices] = mapped_column(Enum(LanguageChoices), default=LanguageChoices.ru)

    seller_user: Mapped[List['Property']] = relationship(back_populates='seller_property',
                                                         cascade='all, delete-orphan')
    rev_author: Mapped[List['Review']] = relationship(back_populates='author_review', foreign_keys='Review.author_id',
                                                      cascade='all, delete-orphan'
    )

    rev_seller: Mapped[List['Review']] = relationship( back_populates='seller_rev', foreign_keys='Review.seller_rev_id',
                                                       cascade='all, delete-orphan'
    )
    user_token: Mapped[List['RefreshToken']] = relationship(back_populates='token_user',
                                                            cascade='all, delete-orphan')


    def __repr__(self):
        return f'{self.role}, {self.preferred_language}'


class Property(Base):
    __tablename__ = "property"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tittle: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text, nullable=True)
    property_type: Mapped[PropertyChoices] = mapped_column(Enum(PropertyChoices), default=PropertyChoices.apartment)
    region: Mapped[str] = mapped_column(String(90))
    city: Mapped[str] = mapped_column(String(60))
    district: Mapped[str] = mapped_column(String(70))
    address: Mapped[str] = mapped_column(String(100))
    area: Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Integer)
    rooms: Mapped[int] = mapped_column(Integer)
    floor: Mapped[int] = mapped_column(Integer)
    total_floors: Mapped[int] = mapped_column(Integer)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    condition: Mapped[ConditionChoices] = mapped_column(Enum(ConditionChoices), default=ConditionChoices.good)
    images: Mapped[str] = mapped_column(String, nullable=True)
    documents: Mapped[str] = mapped_column(String)
    seller_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    seller_property: Mapped[UserProfile] = relationship(UserProfile, back_populates='seller_user')


    def __repr__(self):
        return f'{self.tittle}, {self.property_type}, {self.region}, {self.city}, {self.district}, {self.address}'



class Review(Base):
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    author_review: Mapped[UserProfile] = relationship(UserProfile, back_populates='rev_author', foreign_keys=[author_id])
    seller_rev_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    seller_rev: Mapped[UserProfile] = relationship(UserProfile, back_populates='rev_seller', foreign_keys=[seller_rev_id])
    rating: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


    def __repr__(self):
        return self.comment


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    token_user: Mapped[UserProfile] = relationship(UserProfile, back_populates='user_token')
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f'{self.token}'