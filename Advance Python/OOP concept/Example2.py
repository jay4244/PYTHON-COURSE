"""
in python 
self keyword : other programming it is similar like this keyword

self keyword which is refer current class properties 

this is indicate current class methods and variables.

constructor : in python there is no such keyword like constructor 
   instead of constructor we can use  here __init__()method


   this is behave like same like constructure.


"""
class Student:
    def input(self,name,subject):
        self.name = name
        self.subject = subject

    def display(self):
      print(f"your name is {self.name} and your subject is {self.subject}")  



obj = Student()
obj.input("JAY","PYTHON")

obj.display()