class Student:
    school_name = "ABC School"   # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class method using the @classmethod decorator
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

# Create two student objects
s1 = Student("Ravi", 15)
s2 = Student("Ankita", 16)

print("Before changing:", Student.school_name,s1.name,s1.age)
print("Before changing:", Student.school_name,s2.name,s2.age)

# Call class method to change the school name
Student.change_school("XYZ International School")

print("After changing:", Student.school_name,s1.name,s1.age)
print("After changing:", Student.school_name,s2.name,s2.age)
