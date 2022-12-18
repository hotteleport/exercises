# make a list
basket = ["apple", "banana", "cherry", "carrot", "potato", "tomato", "cabbage"]
new_basket = []
# ask
word = input("Which word to ignore? ")
# if word in the list
if word in basket:
        basket.remove(word)
        new_basket.append(basket)
        print(*basket, sep='\n')
# if human gives a number of fruit
elif word.isnumeric():
    word = int(word)
    word = word - 1
    basket.remove(basket[word])
    new_basket.append(basket)
    print(*basket, sep='\n')
# if word not in the list
elif word not in basket:
    print("Word not found")