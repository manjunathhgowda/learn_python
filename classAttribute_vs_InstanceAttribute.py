class Employee:
    name="Virat"                #class attribute
    sal="2000000"               #class attribute
    role="Software Engineer"    #class attribute

obj=Employee()
print(obj.name,obj.sal,obj.role) 

obj.role="Python Backend Developer"         #Instance attribute has highest preference than class attributes
print(obj.name,obj.sal,obj.role)  