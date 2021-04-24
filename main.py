import random 

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789#@!^:;()"

while 1:
    password_len  = int(input("How long do you want the password to be : "))
    password_count = int(input("How many passwords do you want to generate : "))
    for x in range(0,password_len):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your passowrd", password)
