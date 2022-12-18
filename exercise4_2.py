# ask some word by user
some_text = input("Give some text: \n")
reversed_text = some_text[::-1]
print(reversed_text)
# show result for user
if some_text == "":
    print("Your text is empty")
if some_text == reversed_text:
    print("Palindrome: YES")
if some_text != reversed_text:
    print("Palindrome: NO")