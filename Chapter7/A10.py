
places = {}

polling_active = True

while polling_active:
    name = input("Hello, what's your name? ")
    place = input("If you could go to one place in the world, where would you go? ")
    places[name] = place

    repeat = input("Would another person like to take the poll? [Y]es/[N]o ")
    if repeat == 'N':
        polling_active = False

print("---Poll Results---")
for name, place in places.items():
    print(name + " would like to visit " + place + ".")
