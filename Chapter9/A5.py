
class User():
    def __init__(self, first_name, last_name, job_title, favorite_quote):
        self.first = first_name
        self.last = last_name
        self.job = job_title
        self.quote = favorite_quote
        self.login_attempts = 0
    
    def describe_user(self):
        print(self.first + ' ' + self.last + " is a " + self.job)
        print('Favorite quote: "' + self.quote + '"')

    def greet_user(self):
        print("Hello, " + self.first + "! How are you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Sim', 'Homersin', 'nuclear plant controller', 'Doh!')

print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)