

cubes = [value**3 for value in range(1,11)]
print(cubes)

print("The first three items in the list are: " + str(cubes[0:3]))
print("Three items from the middle of the list are: " + str(cubes[3:7]))
print("The last three items from the list ar: " + str(cubes[len(cubes) - 3: len(cubes)]))