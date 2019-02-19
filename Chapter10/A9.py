
filename_cats = 'cats.txt'
filename_dogs = 'dogs.txt'

try:
    with open(filename_cats, 'r') as f_object:
        cat_lines = f_object.readlines()
except FileNotFoundError:
    pass

try:
    with open(filename_dogs, 'r') as f_object:
        dog_lines = f_object.readlines()
except FileNotFoundError:
    pass

for lines in cat_lines:
    print(lines.rstrip())

for lines in dog_lines:
    print(lines.rstrip())
