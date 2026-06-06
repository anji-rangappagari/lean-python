# instance class variables are variables that are defined inside the class and are shared by all the instances of the class. They are defined using the class name and are accessed using the instance name. They are used to store the data that is common to all the instances of the class.

class Employee:
    company = "Google"  # class variable/attribute that is shared by all the instances of the class

    def __init__(self, name, salary, company):  # constructor is a special function that is called when an object is created. It is used to initialize the object. It is defined using the __init__ keyword. It takes self as the first parameter and other parameters as required.
        self.name = name  # instance variable
        self.salary = salary  # instance variable
        self.company = company  # instance variable

    def get_salry(self):
        return self.salary

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

   
emp1 = Employee("Anjineyulu", 100000, "aws")
print(emp1.company)  # aws
print(emp1.name)  # Anjineyulu
print(emp1.salary)  # 100000