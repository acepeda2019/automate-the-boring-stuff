import pyperclip
import random

def hello(name):
    print(f'Hello! {name}')
    print(f'Howdy There {name}!')
    print(f'Hiya There {name}!\n')

def plusOne(number):
    return number + 1

# hello('Alice')
# print(plusOne(5))



# GLOBAL VS LOCAL SCOPE
# Global variables are defined outside of function and can be accessed by any function
# Local variables are defined exist within a function and can only be accessed within that function

spam = 42 # Global variable

def eggs():
    spam = 500 # Local variable
    print(spam)

print(spam) # This will print 42
print(eggs()) # This will print 500 AND None, spam returns the local value, then the function returns None because return is explicitly called
print(spam) # This will print 42, spam resumes the global value
