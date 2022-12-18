# make a function
def lottery_numbers():
    import random
    collecton = []
    loop = 0
    while loop < 7:
        number = random.randint(1, 40)
        if number in collecton:
            continue
        else:
            collecton.append(number)
            loop = loop + 1
    return collecton

# make a lottery number
lottery_number = lottery_numbers()

# print lottery number
print("Here you can find lottery numbers:")
print(' '.join(map(str, lottery_number)))
