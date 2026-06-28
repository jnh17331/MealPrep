from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    """
    Represents a user profile inside the meal planner.

    This will eventually control:
    - Meal recommendations
    - Grocery lists
    - Dietary substitutions
    - Macro targets
    """

    name: str

    # none, vegetarian, pescatarian, vegan, etc.
    diet: str = "none"

    # Foods the user enjoys
    favorite_foods: List[str] = []

    # Foods the user does not want recommended
    disliked_foods: List[str] = []

    # Allergies/intolerances
    restrictions: List[str] = []

    # Nutrition goals
    calorie_goal: Optional[int] = None
    protein_goal: Optional[int] = None
    fiber_goal: Optional[int] = None

    def summary(self):
        """
        Returns a readable profile summary.
        """

        return {
            "Name": self.name,
            "Diet": self.diet,
            "Favorites": self.favorite_foods,
            "Avoid": self.disliked_foods,
            "Restrictions": self.restrictions,
            "Protein Goal": self.protein_goal
        }