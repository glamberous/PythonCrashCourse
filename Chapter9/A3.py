
class User():
    def __init__(self, first_name, last_name, job_title, favorite_quote):
        self.first = first_name
        self.last = last_name
        self.job = job_title
        self.quote = favorite_quote
    
    def describe_user(self):
        print(self.first + ' ' + self.last + " is a " + self.job)
        print('Favorite quote: "' + self.quote + '"')

    def greet_user(self):
        print("Hello, " + self.first + "! How are you today?")

user1 = User('Sim', 'Homersin', 'nuclear plant controller', 'Doh!')
user2 = User('Charles', 'Tool', 'Robot', 'beep boop')
user3 = User('Grant', 'Lamb', 'Tester', 'Never give up! Never surrender!')

user1.describe_user()
user2.describe_user()
user3.describe_user()