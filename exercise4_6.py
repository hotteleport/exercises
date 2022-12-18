# ask data
temperature = input("Write outside temperature: \n")
temperature = int(temperature)
humidity = input("Write humidity % : \n")
humidity = int(humidity)

# what is false
raining = False
hailstorm = False
heatwave = False
freezing = False

# true condition
if humidity > 80 and temperature > - 20:
    raining = True
elif humidity > 80 and temperature < -20:
    hailstorm = True
elif - 20 < temperature < 0:
    freezing = True
elif temperature > 20:
    heatwave = True
    
# result
if heatwave and raining:
    print("It is damp and hot!")
elif freezing:
    print("It is freezing outside.")
elif hailstorm:
    print("There is a hailstorm, be careful!")
elif heatwave:
    print("Heatwave! Remember to hydrate!")
