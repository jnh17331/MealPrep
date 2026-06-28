from users.questionnaire import run_questionnaire

from database.database import (
    save_user,
    load_users
)


def main():

    user = run_questionnaire()


    save_user(user)


    print("\nUser Saved!\n")


    print("Current Users:")

    users = load_users()

    for user in users:

        print(user)



if __name__ == "__main__":

    main()