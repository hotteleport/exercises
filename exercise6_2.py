# which number?
number = int(input ("Which multiplication table you want to see? (1-10): "))
number == True
# exit conditions:
while number <= 0:
    break
while number > 10:
    print("Wrong number format.")
    break
# true values
if 1 <= number <= 10:
    print ("The Multiplication Table of: ", number)
# calculations
    for count in range(1, 11):
        print (number, 'x', count, '=', number * count)