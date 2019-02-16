
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " has the best " + self.cuisine_type + " food!")
    
    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, new_number):
        self.number_served = new_number
    
    def increment_number_served(self):
        self.number_served += 1

restaurant = Restaurant("Juan's burritos", "Mexican")
print(restaurant.number_served)
restaurant.number_served = 2
print(restaurant.number_served)

restaurant.set_number_served(4)
print(restaurant.number_served)

restaurant.increment_number_served()
print(restaurant.number_served)

