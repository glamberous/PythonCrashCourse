
names = ['Justine', 'Bill', 'Jay']
message = "Please join me for dinner, "
print(message + names[0] + '!')
print(message + names[1] + '!')
print(message + names[2] + '!')
print("We just got more room at our table!")

names.insert(0, 'Juan')
names.insert(2, 'TK')
names.append('Wendy')

print(message + names[0] + '!')
print(message + names[1] + '!')
print(message + names[2] + '!')
print(message + names[3] + '!')
print(message + names[4] + '!')
print(message + names[5] + '!')

print("...Actually our new table won't be arriving in time. I can only invite two people.")
popped_name = names.pop()
print("I'm sorry, " + popped_name + "... You are no longer invited.")
popped_name = names.pop()
print("I'm sorry, " + popped_name + "... You are no longer invited.")
popped_name = names.pop()
print("I'm sorry, " + popped_name + "... You are no longer invited.")
popped_name = names.pop()
print("I'm sorry, " + popped_name + "... You are no longer invited.")
print(names[1] + ", you're still invited!")
print(names[0] + ", you're still invited!")
print(str(len(names)) + " is the number of people who were invited.")
del names[1]
del names[0]
print(names)