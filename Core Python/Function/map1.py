"""
without map
"""

l1 = [1,2,3,4,5]
l2 = []

def myfun(l1):
    for num in l1:
        ans = num + 10
        l2.append(ans)

myfun(l1)
print(l2)

"""
with map
"""

def myfun(num):
    return num + 10

l2 = list(map(myfun,l1))

print(l2)

"""
with map and lambda
"""

l2 = list(map(lambda num : num + 10,l1))

print(l2)