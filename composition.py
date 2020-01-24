"""Composition means delegating some responsibilities from one class to another or part of 
relationship between classes
composition represents part of"""


class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)   # composition instantiating the Salary class

    def total_salary(self):
        return self.obj_salary.annual_salary()


emp = Employee(name='max', age=25, pay=150000, bonus=100000)
print(emp.total_salary())
