"""
Student 
    name 
    subject
    city
    state
    pincode


emp
    name
    department
    city
    state
    pincode
    
=====================
Address:
    city 
    state
    pincode
    
    
    student:
        name
        subject       department
        address       Address    
"""
class Address:
    def __init__(self,city,state,pincode):
        self.city = city
        self.state = state
        self.pincode = pincode
     
class student:
    def __init__(self,name,subject,address):
                self.name = name
                self.subject = subject
                self.address = address
    
    def display(self):            
        print(f"Name :{self.name}")
        print(f"city :{self.address.city}")
        
a1 = Address("thaltej","gujarat",360575)
s1 = student("jay","python",a1)

s1.display()        