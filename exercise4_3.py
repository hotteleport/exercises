text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"
# change world
new_text = text.replace("fox", "duck")
print(new_text)
# removing word
word = input("Which word need be removed? \n")
if word in text:
    text = text.replace(word, '')
    print(text)
else:
    print("Word not found.")
# number of characters
text_length = len(text)
print(f"In the text there are {text_length} characters.")
word_list = text.split()
word_number = len(word_list)
print(f"In the text there are {word_number} words.")
# replace dots
text = text.replace(".", "\n")
print(text)
# ask new sentence
utext = input("Write a new sentence: \n")
utext_lenght = len(utext)
if utext_lenght <= 20:
    print(utext)
else:
    subtext = utext[0:20]
    print(f"{subtext}...")