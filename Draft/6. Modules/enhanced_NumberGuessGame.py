#######################################################################################
# Name of Program: NumberGuessingGame
# Author:         mr-h0n3y
# Purpose:        This program is a simple guessing game where the user tries to guess
#                 a randomly generated number between 1 and 10. It demonstrates the use
#                 of while loops to create interactive loops that continue executing
#                 until a specific condition is met, in this case, the user guessing
#                 the correct number. It also showcases conditional statements and
#                 user input handling in Python.
#######################################################################################

import random
# from random import randint


def guessing_game():

    # In next section we going to make this number random not fixed 
    number_to_guess = random.randint(0, 10)
    guess = None
    
    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 10: "))
        
        if guess < number_to_guess:
            print("Too low, try again.")
        elif guess > number_to_guess:
            print("Too high, try again.")
    
    print("Congratulations! You guessed the right number.")

# Start the game
guessing_game()
