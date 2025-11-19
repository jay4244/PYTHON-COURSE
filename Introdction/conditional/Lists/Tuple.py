"""
 as we konw that tuple is immutable (we can`t change 
"""

t = [10,20,30]
l1 = list(t)
print(t)

l1.append(100)
t =list(l1)
print(l1)