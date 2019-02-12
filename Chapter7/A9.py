
print("Hello, welcome to our sandwich shop.")
print("We are out of pastrami today.")

sandwich_orders = ["Ham", "pastrami", "Peanut Butter and Jelly", "pastrami", "BLT", "Turkey", "pastrami"]
finished_sandwiches = []

while sandwich_orders:
    popped_sandwich = sandwich_orders.pop()
    if popped_sandwich == "pastrami":
        continue
    print("We are making your " + popped_sandwich + " sandwich!")
    finished_sandwiches.append(popped_sandwich)

print(finished_sandwiches)
print("Thanks for playing! Goodbye :)")