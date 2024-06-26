# Number guessing game
import random
from art import logo


def difficulty_level():
    difficulty = input("Chose the difficulty. easy or hard: ")
    if difficulty == "hard":
        return 5
    else:
        return 10


def check_guess(guessed_number, generated_number):
    if guessed_number == generated_number:
        print("Congrats you found the hidden number")
        return True
    elif guessed_number > generated_number:
        print("You are too high")
    else:
        print("You are too low")


def game():
    print(logo)
    print("Welcome to number guessing game")
    print("You need to guess the number between 1 and 100")

    generated_num = random.randint(1, 100)
    end_game = False
    life = difficulty_level()

    while life > 0 and not end_game:
        print(f"You have {life} lives")
        guessed_num = int(input("Guess the number: "))
        end_game = check_guess(guessed_num, generated_num)
        life -= 1

    if life == 0 and not end_game:
        print(f"Ups but the hidden number was {generated_num}")


game()
