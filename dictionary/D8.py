shop ="""
        SHOPPING CART
    samsung s24 : 125999
    vivo v60 : 89999 
    oneplus 9r : 39999
    iphone 13 : 79999
    redmi 10 : 14999
    """ 


cart = {}
print(shop)
status = True
while True:
    product_name = input("Enter product name : ").lower()
    qty = int(input("Enter quantity : "))
    if product_name in shop:
        if product_name == "samsung s24":
            price = 125999
            # cart['product_name'] = "samsung s24"
            # cart['price'] = 125999
            # print(cart)
        elif product_name == "vivo v60":
            price = 89999
        elif product_name == "oneplus 9r":
            price = 39999
        elif product_name == "iphone 13":
            price = 79999
        elif product_name == "redmi 10":
            price = 14999
    else:
        print("Product not aveliable")                    
    Total_price = price * qty    
    cart = print(f"{product_name} Qty. {qty} Rs. :{Total_price}")
    sub_dic = []
    
    ADD = input("Do you want to add more items? (y/n) : ").lower()
    if ADD == 'y' or ADD == 'yes':
        status = True
    else:        
        break
    
    print(cart)  

  