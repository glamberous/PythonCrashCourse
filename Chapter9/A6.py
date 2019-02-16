
import A4

class IceCreamStand(A4.Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'coffee']

    def display_icecream(self):
        print(', '.join(self.flavors))


icecreamstand = IceCreamStand('Dairy Cow', 'Italian')
icecreamstand.display_icecream()