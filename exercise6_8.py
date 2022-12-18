import secrets
import string

# string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


length = True

while length:
    # ask number of password symbols
    length = input("What length of a password you want? \n")
    length = int(length)

    # make a minimum limit
    if length < 8:
        print("The password length should be at least 8 characters.")
        print("Write length again!")
        print()

    # if number pf symbols is ok > make password
    elif length >= 8:
        password = ''.join(secrets.choice(lower + upper + num + symbols) for t in range(length))
        print(f"Your new safe password is ready: {password}")
        length = False