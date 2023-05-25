name_gp1 = {
    "Username": ["Pix",], 
    "Password": ["jUmP?"],
    "Money": 120
}

name_gp2 = {
    "Username": ["Jin"], 
    "Password": ["DuCkErS!"]
}

name_gp3 = {
    "Username": [""], 
    "Password": [""]
}

u = ""

def log_in():
    global u  
    u = input("Username: ")
    p = input("Password: ")
    if u in name_gp1["Username"] or u in name_gp2["Username"] or u in name_gp3["Username"]:
        if p in name_gp1["Password"] and  p in name_gp2["Password"] or u in name_gp3["Username"]:
            print("\\\\\ Log-In Successful /////")
            menu()    
        else:
            print("Credentials Incorrect")
            log_in()
    
    else:
        print("Credentials Incorrect")
        log_in()

def menu():
    print("Welcome " + str(u) + " to the online banking system")
    print("""What would you like to do today:
- Display money
- Take out money
- Deposit money
""")


def sign_up():
    new_u = input("Enter new username: ")
    new_p = input("Enter new password: ")
    if new_u in name_gp1["Username"] or new_u in name_gp2["Username"]:
        print("Username exists")
        sign_up()
    if new_p in name_gp1["Password"] or new_p in name_gp2["Password"]:
        print("Password exists")
        sign_up()
            
    else:
        name_gp3["Username"].append(new_u)
        name_gp3["Password"].append(new_p)
        print("Username and password created")
        log_in()

def options():
    option = int(input("""Select Option
    1. Login
    2. Sign Up
    """))
    if option == 1:
        log_in()
    if option == 2:
        sign_up()

print("Bank Version 1.0")
options()