magicians = ["Alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()} that was a great trick.")

pizzas = ["Cheese", "Chicken", "thin"]

pizzas1 = pizzas[:]

print(pizzas1)

pizzas.append("halal")

pizzas1.append("Italian")

for p in pizzas:
    print(f"My fav pizzas are: {p}")

for p in pizzas1:
    print(f"My fav_ pizzas are: {p}")

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really love pizza")

Animals = ["Cat", "Dog", "Wolf"]

print(Animals)

for animal in Animals:
    print(f"A {animal} would make a great pet")

numbers = []
for i in range(1,1000001):
    numbers.append(i)
    #print(i)

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

for n in range(1,20,2):
    print(n)

val = [n*3 for n in range(1,11)]
print(val)

for num in range(1,11):
    print(f"The cube of {num} is {num**3}" )

cube = [n**3 for n in range(1,11)]
print(cube)

my_foods = ['pizza', 'falafel', 'carrot cake']

friends  = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

for f in my_foods:
    print(f)
