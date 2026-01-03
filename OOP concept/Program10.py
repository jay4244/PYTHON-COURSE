from abc import ABC

class parent(ABC):
    def display(self):
        pass
 
class A(parent):
    def display(self):
        print("Hello from A") 
        
class B(parent):
    def display(self):
        print("Hello from B")
        
a = A()
a.display()
b = B()
b.display()
                   