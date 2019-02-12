
sandwich_orders = ["Ham", "Peanut Butter and Jelly", "BLT", "Turkey"]
finished_sandwiches = []

while sandwich_orders:
    popped_sandwich = sandwich_orders.pop()
    print("We are making your " + popped_sandwich + " sandwich!")
    finished_sandwiches.append(popped_sandwich)

print(finished_sandwiches)
print("Thanks for playing! Goodbye :)")