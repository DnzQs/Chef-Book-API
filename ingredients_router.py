from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.ingredients.ingredient_models import Ingredient
from app.ingredients.ingredient_schemas import IngredientCreate, IngredientResponse

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])


@router.post("/", response_model=IngredientResponse)
def create_ingredient(ingredient: IngredientCreate, db: Session = Depends(get_db)):
    db_ingredient = db.query(Ingredient).filter(Ingredient.name == ingredient.name).first()
    if db_ingredient:
        raise HTTPException(status_code=400, detail="Ingredient already exists")

    new_ingredient = Ingredient(name=ingredient.name)
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient


@router.get("/", response_model=list[IngredientResponse])
def get_all_ingredients(db: Session = Depends(get_db)):
    return db.query(Ingredient).all()