"""
in python itrator is a sequence which it itrate each element line by line.
e.g., list,tuple...

there are 2 function use for iterator
1)_iter_()
2)_next_() 

"""
data = [112,34,23,56,76]

it = iter(data)

print(next(it))
print(next(it))
print(next(it))