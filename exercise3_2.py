# ask tempriture
temperature = input("Give temperature: ")
temperature = int(temperature)
# terms
if 0 <= temperature <= 10:
    print("COLD")
if 11 <= temperature <= 15:
    print("CHILLY")
if 16 <= temperature <= 20:
    print("NORMAL TEMPERATURE")
if 21 <= temperature <= 26:
    print("WARM")
if 26 <= temperature <= 30:
    print("HOT")
