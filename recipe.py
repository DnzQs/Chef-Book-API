from sqlalchemy.orm import Session
from app.recipes.recipe_models import Recipe, RecipeIngredient


def find_recipes_by_ingredients(db: Session, user_ingredient_ids: list[int]):
    potential_recipe_ids = (
        db.query(RecipeIngredient.recipe_id)
        .filter(RecipeIngredient.ingredient_id.in_(user_ingredient_ids))
        .distinct()
        .all()
    )
    recipe_ids = [r[0] for r in potential_recipe_ids]

    if not recipe_ids:
        return {"available_recipes": [], "almost_available_recipes": []}

    recipes = db.query(Recipe).filter(Recipe.id.in_(recipe_ids)).all()

    available_recipes = []
    almost_available_recipes = []
    user_ingredients_set = set(user_ingredient_ids)

    for recipe in recipes:
        missing_ingredients_list = []

        for assoc in recipe.ingredient_associations:
            if assoc.ingredient_id not in user_ingredients_set:
                missing_ingredients_list.append({
                    "id": assoc.ingredient.id,
                    "name": assoc.ingredient.name,
                    "amount": assoc.amount,
                    "unit": assoc.unit
                })

        formatted_recipe = {
            "id": recipe.id,
            "title": recipe.title,
            "description": recipe.description,
            "instructions": recipe.instructions,
            "ingredients": [
                {
                    "id": assoc.ingredient.id,
                    "name": assoc.ingredient.name,
                    "amount": assoc.amount,
                    "unit": assoc.unit
                } for assoc in recipe.ingredient_associations
            ]
        }

        if len(missing_ingredients_list) == 0:
            available_recipes.append(formatted_recipe)
        elif len(missing_ingredients_list) <= 3:
            almost_available_recipes.append({
                "id": recipe.id,
                "title": recipe.title,
                "description": recipe.description,
                "instructions": recipe.instructions,
                "missing_ingredients": missing_ingredients_list
            })

    return {
        "available_recipes": available_recipes,
        "almost_available_recipes": almost_available_recipes
    }