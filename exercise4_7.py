# connect number and text
number_to_word = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
word_to_number = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

parametr = True

# string
# text to number
result = ''
while parametr:
    write = input("Write 0 - 9 in text or number \n")
    if write.replace('','').isalpha():
        print("You wrote: " + write)
        # changing
        result = ''.join(number_to_word[go] for go in write.split())
        print("Text to number : " + result)
        parametr = False
# number to text
    elif write.isnumeric():
        parametr = len(write)
        # make a limit for numbers
        if parametr > 5:
            print(f"MAX is 5")
        elif 1 <= parametr <= 5:
            print("Number: " + write)
            for go in write:
                result = result + word_to_number[go]
                result = result + " "
            print("Result: ", result)
            parametr = False
