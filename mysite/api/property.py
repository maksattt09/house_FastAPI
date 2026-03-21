from fastapi import APIRouter, HTTPException, Depends
from mysite.database.models import Property
from mysite.database.schema import PropertyInputSchema, PropertyOutSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List


property_router = APIRouter(prefix='/properties', tags=['Property'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@property_router.post('/', response_model=PropertyOutSchema)
async def create_property(property: PropertyInputSchema, db: Session = Depends(get_db)):
    property_db = Property(**property.dict())
    db.add(property_db)
    db.commit()
    db.refresh(property_db)
    return property_db


@property_router.get('/', response_model=List[PropertyOutSchema])
async def list_property(db: Session = Depends(get_db)):
    return db.query(Property).all()


@property_router.get('/{property_id}', response_model=PropertyOutSchema)
async def detail_property(property_id: int, db: Session = Depends(get_db)):
    property_db = db.query(Property).filter(Property.id == property_id).first()
    if not property_db:
        raise HTTPException(detail='нету такой информации', status_code=400)
    return property_db


@property_router.put('/{property_id}', response_model=dict)
async def update_property(property_id: int, property: PropertyInputSchema, db: Session = Depends(get_db)):
    property_db = db.query(Property).filter(Property.id == property_id).first()
    if not property_db:
        raise HTTPException(detail='мындай property жок', status_code=400)

    for property_key, property_value in property.dict().items():
        setattr(property_db, property_key, property_value)

    db.commit()
    db.refresh(property_db)
    return {'message': 'property озгорулду'}


@property_router.delete('/{property_id}', response_model=dict)
async def delete_property(property_id: int, db: Session = Depends(get_db)):
    property_db = db.query(Property).filter(Property.id == property_id).first()
    if not property_db:
        raise HTTPException(detail='мындай property жок', status_code=400)

    db.delete(property_db)
    db.commit()
    return {'message': 'property удалит этилди'}