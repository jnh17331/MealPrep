import json
from pathlib import Path

from models.user import User


DATA_FILE = Path("data/users.json")


def initialize_database():
    """
    Makes sure our data files exist.
    """

    DATA_FILE.parent.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")


def save_user(user: User):
    """
    Saves or updates a user profile locally.
    """

    initialize_database()

    users = load_users()

    # Remove existing user with same name
    # This prevents duplicate profiles
    users = [
        existing
        for existing in users
        if existing["name"].lower() != user.name.lower()
    ]

    # Add updated/new user
    users.append(user.model_dump())

    with open(DATA_FILE, "w") as file:
        json.dump(
            users,
            file,
            indent=4
        )


def load_users():
    """
    Loads all saved users.
    """

    initialize_database()

    with open(DATA_FILE, "r") as file:
        users = json.load(file)

    return users