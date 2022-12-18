from functions import *
# ask ISSN
number = input("Give an ISSN-SERIAL:\n")
good_serial = magazine_serial_check(number)
# conditions
if good_serial:
    print("Order code is okay!")
else:
    print("Order code is incorrect.")