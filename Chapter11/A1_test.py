import unittest
from A1 import format_name

class NamesTestCase(unittest.TestCase):
    def test_format_name(self):
        formatted_name = format_name('Seattle', 'Washington')
        self.assertEqual(formatted_name, 'Seattle, Washington')

    def test_format_name_population(self):
        formatted_name = format_name('Los Angeles', 'California', 45000)
        self.assertEqual(formatted_name, 'Los Angeles, California - 45000')

unittest.main()
