import datetime

class GuestBook():
    def __init__(self, filename='guest_book.txt'):
        self.guests = []
        self.filename = filename

    def welcome_user():
        print("Welcome to my guest book! Please sign in!")

    def get_name(self):
        name = input("What is your name? ")
        return name

    def set_new_user(self, guest=''):
        guest = get_name()
        new_user = {'name': guest, 'time': datetime.now()}
        self.guests.append(new_user)

    def save_guest_book(self):
        with open(self.filename, 'w') as file_object:
            file_object.write(self.guests)

    def load_guest_book(self):
        try:
            with open(self.filename, 'r') as file_object:
                content = file_object.read()
        except:
            print("Error in loading profile.")

    def print_book(self):
        print(self.guests)


guest_book = GuestBook
guest_book.welcome_user()
guest_book.get_name()
guest_book.set_new_user()
guest_book.print_book()

