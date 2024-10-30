# GUESSING NUMEBER GAME
# This is a guessing number game where the program generates a random number
# The user guesses a number and the program tells the user if the number is too high or too low
# The user has a limited number of guesses and the answer is revealed if the user runs out of guesses

import random

# GLOBAL VARIABLES
lowerBound = 1
upperBound = 20
randomNumber = random.randint(lowerBound, upperBound)
# randomNumber = 9
guesses = 5

# BEGIN GAME
print('Hello! Welcome to the Guessing Number Game!')
print('What is your name?')

# Error Handling: Ensure that name is non-numeric, ask for name again
while True:
    name = input()
    if name.isalpha() == False:
        print('\nHmm, that does not look like a name. Enter a valid name without numbers.')
    else:
        print(f'\nHello {name}! I am thinking of a number between {lowerBound} and {upperBound}.')
        print(f'You have {guesses} chances to get the correct number. Take a guess! ')
        break

for i in range(1, guesses + 1):
    # Error Handling: Ensure that users guess is an integer, ask to guess again
    while True:
        userGuess = input()
        try:
            userGuess = int(userGuess)
            break
        except ValueError:
            print('Please enter a valid number')

    # Compare the user's guess to the random number
    # User is given hints on whether the number is too high or low and how many guesses they have left
    if i == guesses and userGuess != randomNumber:
        # Answer is revealed if the user runs out of guesses
        print(f'\nYou have run out of guesses! The correct number was {randomNumber}')
    elif userGuess == randomNumber:
        print(f'Congratulations! You guessed the correct number in {i} guesses!')
        break
    elif userGuess < randomNumber:
        print(f'The number is too low! You have {guesses - i} guesses left')
    elif userGuess > randomNumber:
        print(f'The number is too high! You have {guesses - i} guesses left')
        
