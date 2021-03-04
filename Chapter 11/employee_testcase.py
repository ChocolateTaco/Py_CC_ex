# Employee Test Case

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for 'employee.py'."""

    def setUp(self):
        """Creates an employee with a name and salary"""
        self.emp1 = Employee('George', 'Lopez', 50000)

    def test_give_default_raise(self):
        """Gives an employee the default raise amount."""
        self.emp1.give_raise()
        # self.assertEqual(self.emp1.firstname, 'George')
        # self.assertEqual(self.emp1.lastname, 'Lopez')
        self.assertEqual(self.emp1.annual_salary, 50000)

    # def test_give_custom_raise(self):
    #     """Gives an employee a custom raise amount."""
    #     # formatted_city = citycountry('santiago', 'chile', 5000000)
    #     # self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()