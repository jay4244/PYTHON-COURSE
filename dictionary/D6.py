product = {} # main dectionary
costomer ={} # cutomer dectionary
menu = """
        1)product manger 
        2)customer
        3)exit
"""
main_status =True
while main_status:
    print(menu)
    choice=int(input("Enter your choice :"))
    
    if choice==1:
        status=True
        while status:
            sub_dis={}
            product_name =input("Enter product name :")
            product_qty = int(input("Enter your product qty :"))
            product_price =int(input("Enter product price :"))
            
            sub_dis["qty"]=product_qty
            sub_dis["price"]=product_price
            
            product[product_name]=sub_dis
            
            print(product)
            break
    elif choice==2:
        status = True
        while status:
            sub_dis={}
            print("Available products are :")
            for key,value in product.items():
                print(f"Product name : {key} | price : {value['price']} | qty : {value['qty']}")
            Customer_name =input("Enter Customer name :")
            Customer_product =input("Enter product name :")
            Customer_qty = int(input("Enter your product qty :"))
            
            sub_dis ={
                "Customer_name" :Customer_name,
                "product" : Customer_product,
                "qty" : Customer_qty,
                "Bill" : product_price*Customer_qty,
            }
            break
        print("-----------------------------------------")
        print("--------------Customer Bill--------------")
        print("-----------------------------------------")
        for key,value in sub_dis.items():
            print(f"{key}: {value}") 
        print("-----------------------------------------")         
    else:
        main_status=False        