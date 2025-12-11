import m1
menu = """
        1. select for addition
        2. select for multipliction
"""

print(menu)
chioce = int(input("Enter your choice :"))

if chioce == 1:
    print(m1.addition(10,20))
else:
    print(m1.muiltipliction(10,20))
            
