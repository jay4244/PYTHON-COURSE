products ={
    "tv": 15000,
    "mobile" : 5000,
    "leptop" : 75000,
    "ac" : 35000,
    "fridge" : 40000,
}
l2 = list(filter(lambda item : item[1] > 10000 and item[1]< 50000 ,products.items()))
print(l2)