import json
import requests
import var_dump as vd

# Internet data
url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = requests.get(url)
data = req.json()

cities = []
most_warnings_city = ""


for item in data:
    city = item["city"]
    whole_date = item["updated_at"]
    cities.append(city)

def most_frequent(cities):
    return max(set(cities), key = cities.count)

print(f"The city has more warnings than others:" , most_frequent(cities))

print()
print("The latest 5 slippery weather warnings:")
print()

#result
data.sort(key = lambda i: i['updated_at'], reverse = True)
for index in range(5):
    print('City Name: ', data[index]['city'])
    print('Create Time and date: ', data[index]['created_at'])
    print('Update Time and Date: ', data[index]['updated_at'])
    print()
