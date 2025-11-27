menu = """

        MENU 

       VADAPAV  RS. 35
       DABELI   RS. 25
       BHEL     RS. 70
       SANDWICH RS. 120 

"""
cart = {}  #main dictionary
sub_dic = {} # sub dictionary

print(menu)

status = True
while status :
    product_name = input("Enter product name : ").upper()
    qty = int(input("enter qty. ")) 
    
    if product_name == "VADAPAV":
        price = 35
    elif product_name == "DABELI":
        price = 25
    elif product_name == "BHEL":
        price = 70
    elif product_name == "SANDWICH":
        price = 120 


    Total_price = qty * price 

    print(f"product name : {product_name} qty : {qty} Total price : {Total_price}")  

    if product_name in cart.keys():
        sub_dic["qty"] = cart[product_name]["qty"] + qty
        sub_dic["price"] = price

        cart [product_name] = sub_dic

    else :
        sub_dic["qty"] = qty
        sub_dic["price"] = price

        cart[product_name] = sub_dic

        print(cart)
        sum = 0

        choice = input("DO YOU WANT TO CONTINUE ? ")
        if choice == 'n' or choice == 'no':
            status = False

            for k in cart.keys():
                print(f"{k} qty. {cart[k]["qty"]} price : Rs. {cart[k]["qty"] * cart[k]["price"]}")
                sum += cart[k]["qty"] * cart[k]["price"]

            print("--------------------------------------------------")
            print("NET AMOUNT", sum)