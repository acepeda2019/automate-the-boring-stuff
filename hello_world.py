# This program takes name and age then tells users how old they will be next year

# TASKS
# 1. Ask for their name
# 2. Error Handling: Ensure that name is non-numeric, ask for name again
# 3. Ask for their age
# 4. Error Handling: Ensure that age is an integer, ask for age again
# 5. Print out messages that say hi and tell them how old they are next year


print("Hello World!")

print("What is your name?")
while True:
    myName = input()
    # We use a conditional to check if the name is non-numeric
    # If it isn't, repeat the question
    if myName.isalpha():
        break
    else: print("Please enter a valid name without numbers")

print ("What is your age?")
while True:
    myAge = input()
    # We use the try-except block to TRY converting the input to an integer
    # If it fails, we ask for the age again
    try:
        myAge = int(myAge)
        break
    except ValueError:
        print("Please enter a valid number")

print("It's good to meet you, " + myName + "!")
print(f"You are {myAge + 1} years old, next year!") # Cleaner way to print out strings with variables