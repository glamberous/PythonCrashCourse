import datetime
import json

class GatherOpinions():
    def __init__(self, filename='programming_opinions.json'):
        self.opinions = []
        self.filename = filename

    def welcome_user(self):
        print("Welcome to my poll!")

    def get_opinion(self):
        opinion = input("Why do you like programming? ")
        return opinion

    def set_new_opinion(self, opinion):
        self.opinions.append(opinion)

    def save(self):
        with open(self.filename, 'w') as file_object:
            json.dump(self.opinions, file_object)

    def load(self):
        try:
            with open(self.filename, 'r') as file_object:
                self.opinions = json.load(file_object)
        except FileNotFoundError:
            pass
        except Exception as e:
            print("ERROR: " + str(e))

    def print(self):
        print(self.opinions)


poll = GatherOpinions()
poll.load()
poll.welcome_user()
while True:
    opinion = poll.get_opinion()
    if opinion == 'q':
        break
    else:
        poll.set_new_opinion(opinion)
poll.print()
poll.save()

