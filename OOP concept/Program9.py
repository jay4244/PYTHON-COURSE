class A:
    def display(self):
        print("Hello world")
        
class B(A): 
    def display(self):
        A.display(self)
        print("Hello from B")
        
obj = B()
obj.display()                