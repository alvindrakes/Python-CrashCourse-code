import unittest
from Employee import Employee_details

class TestEmployeeDetails(unittest.TestCase):
    """Test for the class Employee.py"""

    def setUp(self):
        """
        create details of the employee
        """
        self.my_employee = Employee_details('Alvin', 'Drakes', 2000)

    def test_give_default_raise(self):
        """test default raise is correct"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 7000)

    def test_give_custom_raise(self):
        """test custom raise is correct"""
        self.my_employee.give_raise(8000)
        self.assertEqual(self.my_employee.annual_salary, 10000)

unittest.main()