# Parent Class
class Animal:
    def speak(self):
        print("Animals make sounds")

# Child Class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")

# Create object of child class
d = Dog()

# Child can use both parent and its own methods
d.speak()  # from Animal class
d.bark()   # from Dog class
