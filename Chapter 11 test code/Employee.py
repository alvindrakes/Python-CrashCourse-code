# 11.3 Employee

class Employee_details():
    """store first name, last name and annual salary"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """raise 5000$ by default but can chnage the raise amount"""
        
        self.annual_salary += amount
        