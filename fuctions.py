def display_message():
 """Display a simple greeting."""
 print("Hello! everyone I am learning functions chapter")
display_message()

def favorite_book(title):
    print(f"One of my favorite book is {title}")

favorite_book("Alice in Wonderland")


def make_shirt(message, size="L"):
    print(f"make a shirt of {size} size and print {message} on it")

make_shirt("L", "Life is full of Love")

make_shirt(size="L",message="Let's learn and Earn")
make_shirt("I love Python")

def describe_city(city, country="India"):
    print(f"{city} is in {country}")

describe_city("Hyderabad")
describe_city("Mumbai")
describe_city(city = "Makkah", country="Saudi")

def city_country(city, country):
    print(f'"{city}, {country}"')

city_country("Hyderabad", "India")
city_country("Chicago", "USA")


def make_album(artist_name, album_title, songs=None):
    album = {"artist": artist_name, "album":album_title}
    if songs:
        album["songs"]=songs
    return album

while True:
    artist = input("Enter artist: ")
    alb = input("Album: ")
    if artist == "quit":
        break
    print(make_album(artist, alb))


mes = ["Hi", "How are u", "Him"]
def show_messages(lis):
    for m in lis:
        print(m)

show_messages(mes)