"""
Genrator : it generate output for the future purpose and return as a iterator

so,using yield keyword and iterator we can generted output.
without genrator :

def myfun():
    return 1
    return 2 x
    
def myfun():
    yield 1
    yield 2
    .
    .
    .    
"""
def myfun():
    yield 1
    yield 2
    yield 3
    
it = myfun()

for i in it:
    print(i)    