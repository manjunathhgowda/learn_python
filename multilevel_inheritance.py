# Grandparent class
class Animal:
    def eat(self):
        print("Animals can eat")

# Parent class
class Dog(Animal):
    def bark(self):
        print("Dog can bark")

# Child class
class Puppy(Dog):
    def weep(self):
        print("Puppy can weep")

# Create object of child class
p = Puppy()

# Access methods from all levels
p.eat()   # from Animal
p.bark()  # from Dog
p.weep()  # from Puppy
