ans = lambda a : a + 10
print(ans(10))

# without lambda

def finder(num) :
    return num * num

print(finder(5))

# with lambda

sqr_ans = lambda num : num * num
print(sqr_ans(5))

ans = lambda num : num%2==0
print(ans(12))