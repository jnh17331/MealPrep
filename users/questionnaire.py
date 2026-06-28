from users.user import User

from nutrition.calculator import calculate_macros



def get_list_input(prompt):

    value = input(prompt)

    return [
        item.strip()
        for item in value.split(",")
        if item.strip()
    ]



def run_questionnaire():


    print("\n======================")
    print(" MealPrep Setup")
    print("======================\n")


    name = input(
        "Name:\n> "
    )


    age = int(
        input(
            "Age:\n> "
        )
    )


    weight = float(
        input(
            "Weight (lbs):\n> "
        )
    )


    height = float(
        input(
            "Height (inches):\n> "
        )
    )


    sex = input(
        "Sex (male/female):\n> "
    )


    print(
"""
Goal:

1. Cut
2. Maintain
3. Bulk
"""
    )


    goal_choice = input("> ")


    goals = {

        "1":"cut",

        "2":"maintain",

        "3":"bulk"

    }


    goal = goals.get(
        goal_choice,
        "maintain"
    )



    activity_level = input(
"""
Activity level:

low
light
moderate
high
very high

> """
    )



    diet = input(
        "Diet type:\n> "
    )


    favorite_foods = get_list_input(
        "Favorite foods:\n> "
    )


    disliked_foods = get_list_input(
        "Foods you dislike:\n> "
    )


    restrictions = get_list_input(
        "Restrictions/allergies:\n> "
    )



    macros = calculate_macros(

        age,

        weight,

        height,

        sex,

        activity_level,

        goal

    )



    print("\nRecommended Daily Targets:")

    for key,value in macros.items():

        print(
            f"{key}: {value}"
        )



    user = User(

        name=name,

        age=age,

        weight=weight,

        height=height,

        sex=sex,

        goal=goal,

        activity_level=activity_level,


        diet=diet,


        favorite_foods=favorite_foods,

        disliked_foods=disliked_foods,

        restrictions=restrictions,


        calorie_goal=macros["calories"],

        protein_goal=macros["protein"],

        carb_goal=macros["carbs"],

        fat_goal=macros["fat"],

        fiber_goal=macros["fiber"]

    )


    return user