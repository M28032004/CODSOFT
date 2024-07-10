print("WELCOME TO RANDOM PASSWORD GENERATOR")
print()


from tkinter import*

import random

import string

def create_password():

    letters = string.ascii_letters
    digits = string.digits
    characters = string.punctuation

    password = " "

    All_characters = (letters+digits+characters)

    
    password ="".join(random.choices(All_characters,k=password_length))


    print(password)

    print()

    print("Your password was generated successfully")

password_length = int(input("Please enter the length of the password:"))

print()    
create_password()

