
names = ['Justine', 'Bill', 'Jay']
message = "Please join me for dinner, "
print(message + names[0] + '!')
print(message + names[1] + '!')
print(message + names[2] + '!')
print("Looks like " + names[1] + " can't make it.")
del names[1]
names.append('Aaron')
print(message + names[0] + '!')
print(message + names[1] + '!')
print(message + names[2] + '!')