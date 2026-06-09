# Chef Book API

A backend REST API for finding recipes based on available ingredients and tracking what is missing.

# Description:
This project is a RESTful API built with FastAPI that allows users to:
* Add and retrieve ingredients from a global database
* Search for recipes based on a custom list of ingredient IDs
* Instantly see recipes that can be cooked right away
* Discover recipes that are almost available (missing 1-3 ingredients) with exact missing amounts and units

# Tech Stack:
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic (Pydantic Settings)
* Docker

# Features:
* Ingredients
  * Create new ingredients
  * Get a list of all available ingredients with their IDs
* Recipes & Matchmaking
  * Smart recipe matchmaking using a Many-to-Many relationship model
  * Categorization of results into fully available and almost available recipes
  * Detailed missing ingredients tracking (ID, name, amount, unit)

# Project structure:
Chef_Book_API/
app/
main.py
core/
config.py
db.py
CRUD/
recipe.py
ingedients/
ingredient_models.py
ingredient_schemas.py
ingredients_router.py
recipes/
recipe_models.py
recipe_schemas.py
recipes_router.py

# Run the Project

* Locally
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic-settings
uvicorn app.main:app --reload

* Using Docker
Choose the directory where the file is downloaded:
docker-compose up --build

# API Documentation
After running the server: http://localhost:8000/docs

# Environment Variables
Create a .env file:
DATABASE_URL=postgresql://postgres:postgres@db:5432/Chef_book_api_db
