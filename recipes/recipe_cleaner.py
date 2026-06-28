import json
from pathlib import Path

from recipes.recipe_model import Recipe


RAW_FILE = Path("recipes/raw/recipes_raw.json")

CLEAN_FILE = Path("recipes/cleaned/recipes_clean.json")


def clean_recipe_data():

    with open(RAW_FILE, "r", encoding="utf-8") as file:
        raw_recipes = json.load(file)


    cleaned = []


    for recipe in raw_recipes:


        name = (
            recipe.get("title")
            or recipe.get("name")
            or "Unknown Recipe"
        )


        instructions = (
            recipe.get("instructions")
            or recipe.get("steps")
            or []
        )


        ingredients = []


        for item in recipe.get("ingredients", []):

            ingredients.append(
                {
                    "name": item
                }
            )


        cleaned_recipe = Recipe(

            name=name,

            ingredients=ingredients,

            instructions=instructions,

            nutrition={},

            tags=[]

        )


        cleaned.append(
            cleaned_recipe.model_dump()
        )


    CLEAN_FILE.parent.mkdir(
        exist_ok=True
    )


    with open(
        CLEAN_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            cleaned,
            file,
            indent=4
        )


if __name__ == "__main__":

    clean_recipe_data()

    print(
        "Recipes cleaned!"
    )