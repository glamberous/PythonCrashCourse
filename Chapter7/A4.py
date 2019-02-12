
toppings = []
user_input = ''
done = False
while not done:
    user_input = input('Input pizza topping (Enter "QUIT" to exit): ')
    if user_input == "QUIT":
        done = True
    else:
        toppings.append(user_input)

print("Thanks for playing!")
print("This is your list of pizza toppings: ")
print(toppings)