
pizzas = ["Cowboy", "Margherita", "Bowery"]
for pizza in pizzas:
    print("I like " + pizza)

print("I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append("Hawaiian")
friend_pizzas.append("Combo")

for pizza in pizzas:
    print("I like " + pizza)

for pizza in friend_pizzas:
    print("My friend likes " + pizza)
