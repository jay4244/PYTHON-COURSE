def factorial(num):
    fact =1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def evenodd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"    