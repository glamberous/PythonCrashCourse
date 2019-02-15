
cities = []

def describe_city(city, country="The United States"):
    temp_dict = {}
    temp_dict['city'] = city
    temp_dict['country'] = country
    cities.append(temp_dict)

done = False
confirmation = 'Y'
while not done:
    city = input("Enter in a city: ")

    confirmation = input("Do you know what country the city is in? Y/N ")
    if confirmation.upper() == 'Y':
        country = input("What country is this city in? ")
        describe_city(city, country)
    else:
        describe_city(city)
    
    confirmation = input("Would you like to enter another city? Y/N ")
    if confirmation.upper() == 'N':
        done = True

for city in cities:
    print(city['city'] + " is in " + city['country'])

