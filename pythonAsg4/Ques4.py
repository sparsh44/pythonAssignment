"""Create a class named Student, use the_init_() function to assign
values for name and roll number. And also call _del_() function to
destroy object that is created."""

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def __del__(self):
        print("Object destroyed")

obj=Student("Sparsh",21103084)

print(obj.name)
print(obj.roll)
del obj
