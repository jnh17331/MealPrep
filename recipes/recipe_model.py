from pydantic import BaseModel
from typing import List, Optional


class Ingredient(BaseModel):
    name: str
    amount: Optional[float] = None
    unit: Optional[str] = None


class Nutrition(BaseModel):
    calories: Optional[int] = None
    protein: Optional[int] = None
    carbs: Optional[int] = None
    fat: Optional[int] = None
    fiber: Optional[int] = None


class Recipe(BaseModel):

    name: str

    ingredients: List[Ingredient]

    instructions: List[str]

    nutrition: Nutrition

    tags: List[str] = []