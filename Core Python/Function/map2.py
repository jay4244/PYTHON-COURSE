l1 = ["python","java","flutter","php"]

l2 = list(map(lambda sub : len(sub),l1))
print(l2)

d1 = dict(map(lambda sub : (sub ,len(sub)),l1))
print(d1)

def myfun(num):
    if num%2==0:
        return True
    else:
        return False
    
l3 = list(map(myfun,l2))
print(l3)

# l2 = list(map(lambda num : num%2==0 ,l2))
# print(l2)    