"""Composition means delegating some responsibilities from one class to another 
Represents a Has-A relationship"""


class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age 
        self.obj_salary = salary 

    def total_salary(self):
        return self.obj_salary.annual_salary()


salary = Salary(150000, 100000)
emp = Employee('max', 25, salary)
print(emp.total_salary())
