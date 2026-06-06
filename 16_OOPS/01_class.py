#  Class: Class is blueprint of object. It is a user defined data type. It is a template for creating objects. It is a collection of variables and functions that are used to represent an object.
#  Object: Object is an instance of a class. It is a real world entity that has state and behavior. It is created from a class. It is a variable that holds the data of the object.


class Employee:
    company = "Google"

    def get_salry(self): # self is a reference variable that refers to the current object. It is used to access the variables and functions of the class. It is a convention to use self as the name of the reference variable.
        return 100000
emp1 = Employee()
print(emp1.get_salry())  # 100000

emp2 = Employee()
print(emp2.get_salry())  # 100000
print(emp1.company)  # Google
print(emp2.company)  # Google