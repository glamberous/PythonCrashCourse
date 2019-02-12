

love = {'first_name':'Justine', 'last_name':'Styles', 'age':35}
best_friend = {'first_name':'Melissa', 'last_name':'White', 'age':30}
coworker = {'first_name':'Juan', 'last_name':'Castro', 'age':34}

people = [love, best_friend, coworker]

for person in people:
    name = (person['first_name'] + ' ' + person['last_name'])
    print('name: ' + name.title())
    print('age: ' + str(person['age']))