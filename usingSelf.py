class Employee:
    name="Virat"                
    sal="2000000"               
    role="Software Engineer"  
    def getInfo(self):
        print(f"Name is {self.name} , Salary is {self.sal} , Role is {self.role}")

obj=Employee()      
obj.getInfo()  # or Employee.getInfo(obj)
