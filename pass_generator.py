#Toprk

from random import randint, choice

letters_string   = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_string   = "0123456789"
symbols_string   = r"!@#$%^&*()_+[];'\,./<>?:\"}{"
password_string  = ""

password = ""

print("(*** PASSWORD GENERATOR V0.1 ***)\n")
"""
    To select the things that you want in your password, press y or Y
    and press enter for those you don't want.
"""

while True:
    #This while loop checks whether the input is an integer or not.
    try:
        pass_min_length = int(input("Enter password MIN length: "))
    except ValueError:
        print("Please type an (+) integer (MIN).")
        continue

    try:
        pass_max_length = int(input("Enter password MAX length: "))
    except ValueError:
        print("Please type an (+) integer (MAX).")
        continue
    #While this one checks whether the MIN value is lower than MAX value or not.
    if pass_min_length > pass_max_length:
        print("MIN length can't be bigger than MAX length.")
        continue
    break


while True:
    #This while loop checks whether the inputs are a string or not.
    letters = input("\nDo you want LETTERS in your pass? (Y/Enter) ")

    try:
        #If the value can be converted into an integer, then it's not a string.
        int(letters)
        print("You should use [Y/Enter]")
        continue
    except ValueError:
        pass

    numbers = input("Do you want NUMBERS in your pass? (Y/Enter) ")

    try:
        int(numbers)
        print("You should use [Y/Enter]")
        continue
    except ValueError:
        pass

    special = input("Do you want SYMBOLS in your pass? (Y/Enter) ")

    try:
        int(special)
        print("You should use [Y/Enter]")
        continue
    except ValueError:
        break

if letters in ("y","Y","yes","YES"):
    password_string += letters_string
if numbers in ("y","Y","yes","YES"):
    password_string += numbers_string
if special in ("y","Y","yes","YES"):
    password_string += symbols_string

try:
    #This for loop makes random selections in random lengths from the password_string.
    for i in range(randint(pass_min_length, pass_max_length)):
        password += choice(password_string)
except IndexError:
    #If nothing is selected, this will be printed:
    print("You have to select at least one. Try Again..")
    quit()

print("\n\tGenerating password...")
print("**************************")
print("SUCCESS! Password:", password)
print("**************************")
