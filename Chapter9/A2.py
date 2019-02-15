
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " has the best " + self.cuisine_type + " food!")
    
    def open_restaurant(self):
        print("The restaurant is open!")

restaurant1 = Restaurant("Juan's burritos", "Mexican")
restaurant2 = Restaurant("Buffalo Wild wings", "American")
restaurant3 = Restaurant("Napakkao", "Thai")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()