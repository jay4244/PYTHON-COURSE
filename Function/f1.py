# without using filter function

l1 = {45,85,65,12,74,54}

l2 = {}

def myfun():
    for i in l1:
        if i%2==0:
            l2.append(i)

myfun()
print(l2)

# with filter function

def myfun(n):
    if n%2==0:
        return n
    
l2 = list(filter(myfun,l1))
print(l2)

# with filter function and with lambda function

l2 = list(filter(lambda n : n%2==0,l1))
print(l2)                
            