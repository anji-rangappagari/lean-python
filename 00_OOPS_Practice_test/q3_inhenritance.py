# 3. Simple Inheritance
# Create a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!".
# Create an object of Dog and call sound().

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")
class Cat(Animal):
    def sound(self):
        print("Meow!")
class Lion(Animal):
    def sound(self):
        print("Roar!")

dog = Dog()
dog.sound()  # Output: Bark!   

cat = Cat()
cat.sound()  # Output: Meow!

lion = Lion()
lion.sound()  # Output: Roar!