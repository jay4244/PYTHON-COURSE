db = {}  # main database

def registration(name, mail, password, subject, city):
    global db
    sub_dis = {
        "name": name,
        "subject": subject,
        "mail": mail,
        "password": password,
        "city": city
    }

    if mail in db:
        return "User already exists!"
    else:
        db[mail] = sub_dis     
        return "Successfully registered!"


def login(mail, password):
    global db
    if mail in db:
        if password == db[mail]["password"]:
            return f"Welcome {db[mail]['name']}!"
        else:
            return "Password does not match"
    else:
        return "Invalid email address"


menu = """
1) Registration
2) Login
"""

status = True
while status:
    print(menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        mail = input("Enter your email: ")
        password = input("Enter your password: ")
        subject = input("Enter your subject: ")
        city = input("Enter your city: ")

        res = registration(name, mail, password, subject, city)
        print("Response:", res)

    elif choice == 2:
        mail = input("Enter your email: ")
        password = input("Enter your password: ")

        res = login(mail, password)
        print("Response:", res)

    else:
        print("Invalid choice!")

    print("--------------------------")
    choice_exit = input("Do you want to perform more operations? (y/n): ").lower()

    if choice_exit == "n":
        status = False
