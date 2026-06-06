#  constrcutors are used to initialize the object of the class

class Employee:
    company = "Google"

    def __init__(self, name, salary):  # constructor is a special function that is called when an object is created. It is used to initialize the object. It is defined using the __init__ keyword. It takes self as the first parameter and other parameters as required.
        self.name = name  # self.name is an instance variable that is used to store the name of the employee. It is initialized using the constructor.
        self.salary = salary  # self.salary is an instance variable that is used to store the salary of the employee. It is initialized using the constructor.

    def get_salry(self):
        return self.salary  # self.salary is used to access the salary of the employee. It is returned by the get_salary function.
    def get_name(self):
        return self.name  # self.name is used to access the name of the employee. It is returned by the get_name function.  
    def get_company(self):
        return self.company  # self.company is used to access the company of the employee. It is returned by the get_company function.
emp1 = Employee("Anjineyulu", 100000)
print(emp1.get_salry())  # 100000
print(emp1.get_name())  # Anjineyulu
print(emp1.get_company())  # Google