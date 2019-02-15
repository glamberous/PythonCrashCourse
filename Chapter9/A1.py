
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " has the best " + self.cuisine_type + " food!")
    
    def open_restaurant(self):
        print("The restaurant is open!")

restaurant = Restaurant("Juan's burritos", "Mexican")
restaurant.describe_restaurant()
restaurant.open_restaurant()