
valid_input = False
while valid_input == False:
    user_input = input("Enter a number: ")
    try:
        user_input = int(user_input)
    except:
        print("Input wasn't a number!")
        continue
    valid_input = True

if (user_input % 10) == 0:
    print("Your number is a multiple of 10!")
else:
    print("Not a multiple of ten.\nTry Again.")