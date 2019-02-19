class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        try:
            self.salary = int(salary)
        except:
            print("INVALID INPUT: salary - defaulting to 20000")
            self.salary = 20000
    
    def give_raise(self, salary_raise=5000):
        self.salary += salary_raise

    
