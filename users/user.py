from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):

    name: str

    age: int

    weight: float

    height: float

    sex: str


    goal: str

    activity_level: str


    diet: str = "none"


    favorite_foods: List[str] = []

    disliked_foods: List[str] = []

    restrictions: List[str] = []


    calorie_goal: Optional[int] = None

    protein_goal: Optional[int] = None

    carb_goal: Optional[int] = None

    fat_goal: Optional[int] = None

    fiber_goal: Optional[int] = None