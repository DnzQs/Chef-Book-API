from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.CRUD.recipe import find_recipes_by_ingredients
from app.recipes.recipe_schemas import FindRecipesRequest, FindRecipesResponse

router = APIRouter(prefix="/recipes", tags=["Recipes"])

@router.post("/find-by-ingredients", response_model=FindRecipesResponse)
def find_recipes(payload: FindRecipesRequest, db: Session = Depends(get_db)):
    return find_recipes_by_ingredients(db, payload.ingredient_ids)