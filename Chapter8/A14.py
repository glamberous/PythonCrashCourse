
def build_car(make, model, **car_info):
    """Build a dictionary containing a cars specs."""
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

my_car = build_car('toyota', 'rav4', year=1996, color='green', awesome=True)
print(my_car)