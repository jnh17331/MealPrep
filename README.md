# MealPrep

MealPrep is a personalized meal planning application designed to generate food recommendations based on:

- User goals
- Body metrics
- Activity levels
- Dietary preferences
- Food restrictions
- Macro targets

The long-term goal is to create a flexible meal recommendation system that can run locally, through a browser, or eventually as a mobile application.

---

# Current Features

## User Profile System

Users can create profiles containing:

- Name
- Age
- Weight
- Height
- Sex
- Goal:
  - Cutting
  - Maintaining
  - Bulking

- Activity level
- Diet preference
- Favorite foods
- Disliked foods
- Allergies/restrictions

---

## Macro Calculator

The application currently calculates recommended:

- Calories
- Protein
- Carbohydrates
- Fat
- Fiber

Based on:

- BMR
- Activity multiplier
- Goal adjustment

Goals supported:

### Cut
Calorie deficit

### Maintain
Maintenance calories

### Bulk
Calorie surplus

---

# Current Project Structure

```text
food_rec/

│
└── app.py
└── requirements.txt
└── README.md
│
├── data/
|   └── ingredients.json
|   └── meals.json
|   └── users.json
|
├── database/
│   ├── __pycache__
│   └── __init__.py
│   └── database.py
│
├── models/
│   ├── __pycache__
│   └── __init__.py
│   └── user.py
|
├── nutrition
│   ├── __pycache__
|   └── __init__.py
│   └── calculator.py
|
├── recipes/
│   │
│   ├── adapters/
|   |
│   ├── cleaned/
│   │   └── recipes_clean.json
|   |
│   ├── raw/
│   │   └── recipes_raw.json
│   │
│   │
│   └── recipe_cleaner.py
│   └── recipe_loader.py
│   └── recipe_model.py
|
├── services/
|   └── __init__.py
|   └── macro_calculator/py
|   └── meal_engine.py
|   └── shopping_list.py
|
├── ui/
|   └── __init__.py
│   └── main_window.py
|
├── users/
│   ├── __pycache__
│   └── __init__.p
│   └── questionnaire.py
│   └── user.py
│
│
└── utils/
    └── __init__.py
    └── helpers.py
```

---

# Recipe Pipeline

Current planned workflow:

Dataset
↓
Raw Recipe Storage
↓
Recipe Cleaner
↓
Standardized Recipe Model
↓
Clean Recipe Database
↓
Recommendation Engine

---

# Recipe Cleaning Goals

Recipes should eventually standardize:

- Recipe name
- Ingredients
- Measurements
- Instructions
- Nutrition information
- Tags
- Cuisine
- Meal type

The cleaner should support different external datasets.

Possible sources:

- Food.com datasets
- NLP recipe datasets
- Kaggle recipe datasets
- Open food databases

---

# Future Goals

## Recommendation Engine

Generate recipes based on:

User profile

+
 
Recipe database

+

Macro targets

+

Preferences


Example:

User:
- Cutting
- High protein
- Dislikes seafood

Output:

- High protein chicken meals
- Macro aligned recipes
- Avoid disliked foods


---

# Future Platforms

Planned support:

## Local Browser App

Possible stack:

- FastAPI backend
- React frontend

---

## Mobile Application

Possible options:

- React Native
- Flutter

---

# Development Environment

Environment:

conda environment:

mealprep

Python:

3.13

Run:

conda activate mealprep

python app.py

---

# Current Development Phase

Phase 1:
Completed

- Project setup
- Conda environment
- User system
- Database storage
- Macro calculation

Phase 2:
Current

Recipe ingestion and cleaning system

Phase 3:

Recommendation engine

Phase 4:

Web interface

Phase 5:

Mobile application

---

# Author

Jesse Heaton
