menu ="""

          MENU
    VADAPAV   Rs. 35
    DABILI    Rs. 25
    BHEL      Rs. 70
    SANDWHICH Rs. 100      
"""
cart ={} # main dictionary

print(menu)
status = True
while status:
    product_name = input("Enter product name : ").upper()
    quantity = int(input("Enter quantity : "))
    if product_name == "VADAPAV":
        price = 35
    elif product_name == "DABILI":
        price = 25
    elif product_name == "BHEL":
        price = 70
    elif product_name == "SANDWHICH":
        price = 100
    
    total_price = price * quantity
    
    print(f"{product_name} Qty. {quantity} Rs. : {total_price}")

