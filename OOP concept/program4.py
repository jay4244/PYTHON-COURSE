class student:
    def __init__(self,name,subject,score):
       self.name = name
       self.subject = subject
       self.score = score
       
    def display(self):
        print(f"name = {self.name}")
        print(f"subject = {self.subject}")
        print(f"score = {self.score}")

name = input("Enter your name :")
subject = input("Enter your subject :")
score = int(input("Enter your score :"))
        
obj = student(name,subject,score)    

obj.display()
            