import unittest
from A3 import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.new_employee = Employee('Grant', 'Lamb', 55000)

    def test_default_raise_test(self):
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 60000)

    def test_custom_raise_test(self):
        self.new_employee.give_raise(2000)
        self.assertEqual(self.new_employee.salary, 57000)


unittest.main()

    
