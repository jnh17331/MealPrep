def calculate_macros(
    age,
    weight,
    height,
    sex,
    activity_level,
    goal
):
    """
    Calculates daily calorie and macro targets.

    Uses:
    Mifflin-St Jeor BMR formula
    """

    # Convert pounds to kg
    weight_kg = weight * 0.453592

    # Convert inches to cm
    height_cm = height * 2.54


    # BMR calculation

    if sex.lower() == "male":

        bmr = (
            10 * weight_kg
            + 6.25 * height_cm
            - 5 * age
            + 5
        )

    else:

        bmr = (
            10 * weight_kg
            + 6.25 * height_cm
            - 5 * age
            - 161
        )


    activity_multiplier = {

        "low": 1.2,

        "light": 1.375,

        "moderate": 1.55,

        "high": 1.725,

        "very high": 1.9

    }


    maintenance = (
        bmr
        *
        activity_multiplier.get(
            activity_level.lower(),
            1.55
        )
    )


    # Goal adjustment

    if goal.lower() == "cut":

        calories = maintenance - 500


    elif goal.lower() == "bulk":

        calories = maintenance + 300


    else:

        calories = maintenance



    # Macro targets

    protein = weight * 1


    fat = (
        calories * 0.25
    ) / 9


    protein_calories = protein * 4

    fat_calories = fat * 9


    carbs = (
        calories
        -
        protein_calories
        -
        fat_calories
    ) / 4


    fiber = (
        calories / 1000
    ) * 14


    return {

        "calories": round(calories),

        "protein": round(protein),

        "carbs": round(carbs),

        "fat": round(fat),

        "fiber": round(fiber)

    }