person = {'f_name':'Asfiya', 'l_name':'Begum', 'age':30, 'status':'student'}

print(person['f_name'],person['l_name'],person['age'], person['status'])

nums = {'Baseer': [7,8], 'Isra': [2,55], 'Asfiya': [5,564]}

print(nums)

glossary = {"Linear":"a regression model", "string": "a data type", 
            "tuple":"again data type", "list": "data type","error":"got an error"}

print(glossary)

for key, value in glossary.items():
    print(f'word: {key}')
    print(f'meaning: {value}')

rivers = {'Nile':"Egypt", "Dead Sea": "Lowest point on earth", "Ocean": "Pacific"}

for r,p in rivers.items():
    if r.lower() == "nile":
        print(f"The {r} runs through {p}")
    elif r.lower() =="dead sea":
        print(f"you know {p} is {r}")
for key in rivers.keys():
    print(key)
for value in rivers.values():
    print(value)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

poll = ["Baseer", "Tahseen", "Mateen", "jen", "sarah"]

for p in poll:
    if p in favorite_languages:
        print(f"Thanks for taking poll {p}")
    else:
        print(f"Please take the poll {p}")

person1 = {'f_name':'Baseer', 'l_name':'Mohammed', 'age':34, 'status':'Entreprenuer'}

person2 = {'f_name':'Isra', 'l_name':'Baseer', 'age':2, 'status':'Badmashi'}

all = [person, person1, person2]

for a in all:
    print(a)

fav_places = {"Baseer": ["USA", "Canada", "Saudi"], 
              "Asfiya": ["India", "saudi", "USA"], "Isra": ["USA", "India", "Hyd"]}

for key,value in fav_places.items():
    print(f"{key} your fav places are:")
    print(f"\t{value}")


cities = {
    "Hyderabad":{
        "Country": "India",
        "Pop":11,
        "fact": "My Hometown"
    },
    "Makkah" : {
        "Country": "Saudi",
        "pop": 5,
        "fact":"My dream"
    },
    "Madinah": {
        "Country": "Saudi Arabia",
        "pop": 6,
        "fact":"Where I wanna spend every second of my life after hajj"
    }
}

for key, values in cities.items():
    print(f"{key}: {values}")

nums = {'Baseer': [7,8], 'Isra': [2,55], 'Asfiya': [5,564]}

print(nums)