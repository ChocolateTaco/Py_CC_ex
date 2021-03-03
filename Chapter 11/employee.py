# 11-3. Employee

class Employee:
    def __init__(self, firstname, lastname, annual_salary):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary

    def give_raise(self, raise=5000):
        self.annual_salary += self.raise            # Still have to work on this method. Getting errors


emp1 = Employee('Regis', 'Kelly', 12000)
print(emp1.firstname)
