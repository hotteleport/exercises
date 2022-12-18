# ask a numbers
try:
    number = input("Give a number one:\n")
    number = int(number)
    print(f"First number: {number}")
    number2 = input("Give a number two:\n")
    number2 = int(number2)
    print(f"Second number: {number2}")
    result = number / number2
    print(f"Your result: {result}")
# add except errors
except ValueError:
    print("You wrote text! Run the application again.")
except ZeroDivisionError:
    print("You can't divide by zero.")