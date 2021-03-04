# 11-3. Employee

class Employee:
    def __init__(self, firstname, lastname, annual_salary):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary

    def give_raise(self, raise_amt):
        if raise_amt:
            self.annual_salary += 5000            # Still have to work on this method. Getting errors
        else:
            self.annual_salary += raise_amt

emp1 = Employee('Regis', 'Kelly', 12000)
print(emp1.firstname)
