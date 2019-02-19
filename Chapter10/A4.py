import datetime
import json

class GuestBook():
    def __init__(self, filename='guest_book.json'):
        self.guests = []
        self.filename = filename

    def welcome_user(self):
        print("Welcome to my guest book! Please sign in!")

    def get_name(self):
        name = input("What is your name? ")
        return name

    def set_new_user(self, guest):
        now = datetime.datetime.now()
        new_user = {'name': guest, 'time': str(now)}
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


guest_book = GuestBook()
guest_book.load()
guest_book.welcome_user()
while True:
    name = guest_book.get_name()
    if name == 'q':
        break
    else:
        guest_book.set_new_user(name)
guest_book.print()
guest_book.save()

