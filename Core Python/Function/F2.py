def addition():
    num1 = int(input("Enter your number :"))
    num2 = int(input("Enter your number :"))
    ans = num1 + num2
    print(ans)
    
def multipliction():
    num1 = int(input("Enter your number :"))
    num2 = int(input("Enter your number :"))
    ans = num1 * num2
    print(ans)
    
menu = """
            MENU:
        1) addition
        2)multipliction    
"""    
print(menu)
choice = int(input("Enter your choice :"))
if choice == 1:
    addition()
elif choice == 2:
    multipliction()
else:
    print("INVALID INPUT")        