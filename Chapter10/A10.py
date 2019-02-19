
filename_pride = 'PrideAndPrejudice.txt'
filename_frankenstein = 'Frankenstein.txt'
filename_drjekyll = 'DrJekyll.txt'

try:
    with open(filename_pride, encoding="utf8") as f_object:
        contents = f_object.read()
except FileNotFoundError:
    pass

print(filename_pride + ": " + str(contents.lower().count('the')))

try:
    with open(filename_frankenstein, encoding="utf8") as f_object:
        contents = f_object.read()
except FileNotFoundError:
    pass

print(filename_frankenstein + ": " + str(contents.lower().count('the')))

try:
    with open(filename_drjekyll, encoding="utf8") as f_object:
        contents = f_object.read()
except FileNotFoundError:
    pass

print(filename_drjekyll + ": " + str(contents.lower().count('the')))