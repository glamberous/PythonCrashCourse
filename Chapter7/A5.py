
print("Welcome to the movies!")

user_input = ''
message = "Your ticket price is $"
done = False
while not done:
    user_input = input('Enter your age (Enter "QUIT" to exit): ')
    if user_input == "QUIT":
        done = True
    else:
        try:
            user_input = int(user_input)
        except:
            print("User input wasn't a number. Try again~")
            continue
        if user_input <= 3:
            price = 0
        elif user_input > 3 and user_input < 12:
            price = 10
        elif user_input >= 12:
            price = 15
        print(message + str(price))
            
print("Thanks for playing! Goodbye :)")