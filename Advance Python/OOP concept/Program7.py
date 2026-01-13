class student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    def setname(self,name):
        self.name = name
        
    def getname(self):
        return self.name
    
    def setscore(self,score):
        self.score = score
     
    def getscore(self):
        return self.score
    
obj = student("jay",78)

print(obj.getname())

obj.setname("milan")

print(obj.getscore())                