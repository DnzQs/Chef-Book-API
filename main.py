from fastapi import FastAPI
from app.core.db import engine, Base

from app.ingredients.ingredients_router import router as ingredients_router
from app.recipes.recipes_router import router as recipes_router

from app.ingredients.ingredient_models import Ingredient
from app.recipes.recipe_models import Recipe, RecipeIngredient

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Chef Book API",
    description="API для поиска рецептов по имеющимся ингредиентам",
    version="1.0.0"
)

app.include_router(ingredients_router, prefix="/api/v1")
app.include_router(recipes_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome     to Chef Book API! Go to /docs for Swagger."}