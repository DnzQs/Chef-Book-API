from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class RecipeIngredientDetail(BaseModel):
    id: int
    name: str
    amount: float
    unit: str
    model_config = ConfigDict(from_attributes=True)

class RecipeBase(BaseModel):
    title: str
    description: Optional[str] = None
    instructions: str

class RecipeResponse(RecipeBase):
    id: int
    ingredients: List[RecipeIngredientDetail]
    model_config = ConfigDict(from_attributes=True)

class FindRecipesRequest(BaseModel):
    ingredient_ids: List[int]

class MatchRecipeResult(RecipeBase):
    id: int
    missing_ingredients: List[RecipeIngredientDetail]
    model_config = ConfigDict(from_attributes=True)

class FindRecipesResponse(BaseModel):
    available_recipes: List[RecipeResponse]
    almost_available_recipes: List[MatchRecipeResult]
