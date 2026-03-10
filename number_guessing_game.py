# Python number guessing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("This is a number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter a guess: ")

    if guess.isdigit:
        guess = int(guess)
        guesses += 1

        if guess < lowest_num and guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between{lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"CORRECT! The answer is {answer}")
            print(f"The number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid input")
        print(f"Please select a number between {lowest_num} and {highest_num}")