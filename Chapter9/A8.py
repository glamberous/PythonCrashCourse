
import A5

class Admin(A5.User):
    def __init__(self, first_name, last_name, job_title, favorite_quote):
        super().__init__(first_name, last_name, job_title, favorite_quote)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ['can ban user', 'can delete posts', 'can add post']

    def show(self):
        print(', '.join(self.privileges))

admin = Admin('Grant', 'Lamb', 'Tester IV', 'Close Range?!')
admin.privileges.show()