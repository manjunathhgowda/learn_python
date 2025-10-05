# Parent class 1
class Father:
    def skill1(self):
        print("Father: Knows driving")

# Parent class 2
class Mother:
    def skill2(self):
        print("Mother: Knows cooking")

# Child class inherits from both
class Child(Father, Mother):
    def skill3(self):
        print("Child: Knows dancing")

# Create object of Child
c = Child()

# Access methods from both parents + child
c.skill1()
c.skill2()
c.skill3()


# Python follows an order called MRO (Method Resolution Order) —
# it decides which parent’s method to call first when names conflict.

# Example (same method in both parents):

class A:
    def show(self):
        print("From class A")

class B:
    def show(self):
        print("From class B")

class C(A, B):
    pass

obj = C()
obj.show()
