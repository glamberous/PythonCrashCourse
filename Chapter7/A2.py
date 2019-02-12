
valid_input = False
while valid_input == False:
    dinner_group_num = input("How many people are in your dinner group? ")
    try:
        dinner_group_num = int(dinner_group_num)
    except:
        print("Input wasn't a number!")
        continue
    valid_input = True

if dinner_group_num > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready!")