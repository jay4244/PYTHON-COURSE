"""
Encapsulation prevent data from outside the uses
which is provide getter and setter methods.

there 3 visibility mode in python

1) public : which is indepedantly access from outside the class
2) private : which is access inside the own class only 
             private which is indicate by __(double underscore in prefix)
3) procted :              
"""
class Product:
    def __init__(self):
        self.mobile = 15000        # public member
        self.__leptop = 25000      # private member

    def display(self):
        print("Mobile price:", self.mobile)
        print("Laptop price:", self.__leptop)

    def changeprice(self, price):
        self.__leptop = price     # modifying private member safely


obj = Product()

obj.display()

obj.mobile = 30000        
obj.__leptop = 40000  

obj.display()            

obj.changeprice(45000)   
obj.display()
