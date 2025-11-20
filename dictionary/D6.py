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
    elif choice==2:
        sub_dis={}
        while status:
            sub_dis={}
            Customer_name =input("Enter product name :")
            product_qty = int(input("Enter your product qty :"))
            product_price =int(input("Enter product price :"))
            
            sub_dis["qty"]=product_qty
            sub_dis["price"]=product_price
            
        
            print(costomer)   
    else:
        main_status=False        