import json
from pathlib import Path

from recipes.recipe_model import Recipe


CLEAN_FILE = Path("recipes/cleaned/recipes_clean.json")


def load_recipes():

    if not CLEAN_FILE.exists():
        return []


    with open(CLEAN_FILE, "r") as file:

        data = json.load(file)


    recipes = [
        Recipe(**recipe)
        for recipe in data
    ]


    return recipes



if __name__ == "__main__":

    recipes = load_recipes()

    print(f"Loaded {len(recipes)} recipes")

    for recipe in recipes[:3]:
        print(recipe.name)