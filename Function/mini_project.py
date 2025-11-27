db ={} # main database

def registration(name,mail,password,subject,city):
    global db
    sub_dis ={}
    sub_dis["name"] = name 
    sub_dis["subject"] = subject
    sub_dis["mail"] = mail
    sub_dis["password"] = password
    sub_dis["city"] = city
    
    if mail in db.keys():
        return "user already exists !."
    else:
        return "succesfuly registration done ."
    
def login(mail,password):
    global db
    if mail in db.keys():
        if password == db[mail]["password"]:
            return f"welcome {db[mail]["name"]}"
        else:
            return "password does not match"
    else:
        return "invalid mail address"
    
menu = """
        1)registration
        2)login

"""        
status = True
while status:
    print(menu)
    choice = int(input("Enter your chioce :"))
    if choice == 1:
        name = input("Enter your name :")
        mail = input("Enter your mail :")
        password = int(input("Enter your password :"))
        subject = input("Enter your subject :")
        city = input("Enter your city :")
        
    res = registration(name,mail,password,subject,city)
    
    print("Response :",res)
    
else:
    mail = input("Enter your mail :")
    password = input ("Enter your password :")
    
    res = login(mail,password)
    
    print(res) 
    
    print("--------------------------")
    
    choice_exit = input("do you wnat so perform more operations ? press 'y' or 'n'").lower()
    if choice_exit == 'n' or choice_exit == 'no':
        status =False   
