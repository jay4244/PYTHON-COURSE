"""
 as we konw that tuple is immutable (we can`t change 
"""

t = (10,20,30)
l1 = list(t)
print(l1)

l1.append(1001)
t=tuple(l1)
print(t)