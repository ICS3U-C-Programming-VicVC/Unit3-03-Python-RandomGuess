#!/usr/bin/env python3
# Created By: Victor V-C
# Date: 10 15, 2026
# This file where constants are stored for num_guess.py


import random


def main():

    # Get the correct generated number frm 1-10
    correct_number = random.randint(1, 10)

    # Get a guessed number from the user
    guessed = int(input("Guess a random number in the range of 1-10: "))

    # check if the number is the same as the correct number

    if guessed == correct_number:

        # If correct then tell the user they guessed correctly
        print("You Guessed Correctly!")

    if guessed != correct_number:

        # If not correct then tell the user they guessed incorrectly
        print("You Guessed Incorrectly!")
        print("The correct number was: {}".format(correct_number))


if __name__ == "__main__":
    main()
