class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
        

# storing employee details

e1=Employee("Mehak",40000)
e2=Employee("Ashok",50000)
e3=Employee("Viren",60000)



#Part a
print("Part a")
e1.salary=70000
print(f"The updated salary of {e1.name} is {e1.salary} ")
#part b
print("Part b")
del e3
print("Record of Viren is deleted")