class Employee:
    name="Virat"        #class attribute
    sal="2000000"       #class attribute

obj=Employee()
obj.role="Python Backend Developer"         #Instance attribute
print(obj.name,obj.sal,obj.role)            # Virat 2000000 Python Backend Developer
#-----------------------------------------------------------------------------------------

#using constructor

class Car:
    wheels=4        #class attribute
    def __init__(self,brand,color):
        self.brand=brand    #Instance attribute
        self.color=color    #Instance attribute

c1=Car("Tesla","Red")
c2=Car("BMW","Black")
print(c1.wheels,c2.wheels)  # 4 4
print(c1.brand,c1.color)    # Tesla Red
print(c2.brand,c2.color)    # BMW Black

Car.wheels=6                #class attribute share by all instances,change affects to all object

print(c1.wheels,c2.wheels)  # 6 6
print(c1.brand,c1.color)    # Tesla Red
print(c2.brand,c2.color)    # BMW Black

