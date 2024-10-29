# Try and Except statements are used to handle errors in Python

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

# Return a message based on the number of cats a user has
# Validate the input so that the user cannot enter a negative number
# Validate the input so that the user cannot enter a string
# Continue to ask for input until a valid number is entered

while True:
    numCats =  input('\nHow many cats do you have? ')
    try:    
        if int(numCats) < 0:
            print('You cannot have negative cats!')
            continue # This will skip the rest of the code and start the loop again
        elif int(numCats) >= 4:
            print('That is a lot of cats!')
        else:
            print('That is not that many cats!')
        break # this will end the while loop after the if statement is executed
    except ValueError:
        print('Please enter a valid number')