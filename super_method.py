# Parent class
class Parent:
    def display(self):
        print("This is the Parent class")

# Child class
class Child(Parent):
    def display(self):
        # Call the parent class method using super()
        super().display()
        print("This is the Child class")

# Create object of Child class
obj = Child()
obj.display()
