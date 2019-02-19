import datetime
import json

class FavoriteNumbers():
    def __init__(self, filename='favorite_numbers.json'):
        self.guests = []
        self.filename = filename

    def welcome_user(self):
        print("Welcome to my guest book! Please sign in!")

    def get_name(self):
        name = input("What is your name? ")
        return name

    def get_favorite_number(self):
        favorite_number = input("What is your favorite number? ")
        return favorite_number

    def set_new_user(self, guest):
        fav_num = self.get_favorite_number()
        now = datetime.datetime.now()
        new_user = {'name': guest, 'time': str(now), 'fav_num': fav_num}
        self.guests.append(new_user)

    def save(self):
        with open(self.filename, 'w') as file_object:
            json.dump(self.guests, file_object)

    def load(self):
        try:
            with open(self.filename, 'r') as file_object:
                self.guests = json.load(file_object)
        except Exception as e:
            print("ERROR: " + str(e))

    def print(self):
        print(self.guests)

    def find(self, name):
        for guest in self.guests:
            if guest['name'] == name:
                return guest
        else:
            return None

guest_book = FavoriteNumbers()
guest_book.load()
guest_book.welcome_user()
while True:
    name = guest_book.get_name()
    guest = guest_book.find(name)
    if name == 'q':
        break
    elif guest:
        print("Your favorite number is " + guest['fav_num'] + "!")
    else:
        guest_book.set_new_user(name)
guest_book.print()
guest_book.save()

