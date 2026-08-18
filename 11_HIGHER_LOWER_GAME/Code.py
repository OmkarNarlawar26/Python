# Display art
from Art import logo, vs
from game_data import data

import random
import os

print(logo)


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
        # if user_guess == "a":
        #     return True
        # else:
        #    return False
    else:
        return user_guess == "b"

def play_game():
    score = 0
    game_should_continue = True
    # Generate a random account from the game data
    account_b = random.choice(data)

    # Make the game repeatable.
    while game_should_continue:

        # Making account at position B become the next account at position A.
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Clear the screen
        os.system("cls" if os.name == "nt" else "clear")

        # - Get follower count of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct.
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Give user feedback on their guess.
        # score keeping.
        if is_correct:
            score += 1
            print(f"You're right! Current score {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_should_continue = False

while True:
    play_game()
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break

    os.system("cls" if os.name == "nt" else "clear")
    print(logo)