#List of dictionaries with users log-in info
name_gp1 = {
    "Username": ["Pix",], 
    "Password": ["jUmP?"],
    "Money": 120,
    "Code": 2385
}

name_gp2 = {
    "Username": ["Jin"], 
    "Password": ["DuCkErS!"],
    "Money": 54,
    "Code": 6937

}

name_gp3 = {
    "Username": [""], 
    "Password": [""],
    "Money": 0,
    "Code": []
    
    }

u = ""

#The basic log-in feature which scans the dicts to see if the username and passwords are there.
def log_in():
    global u  
    u = input("Username: ")
    p = input("Password: ")
    if u in name_gp1["Username"] or u in name_gp2["Username"] or u in name_gp3["Username"]:
        if p in name_gp1["Password"] or p in name_gp2["Password"] or u in name_gp3["Username"]:
            print("\\\\\ Log-In Successful /////")
            menu()    
        else:
            print("Credentials Incorrect")
            log_in()
    
    else:
        print("Credentials Incorrect")
        log_in()

#Display Money or dm scans the dicts to look for the code and then outputs the money in the account
def dm():
    code = int(input("Code: "))
    if code == name_gp1["Code"]:
        print(name_gp1["Money"])
        menu()
    elif code == name_gp2["Code"]:
        print(name_gp2["Money"])
        menu()
    elif code == name_gp3["Code"]:
        print(name_gp3["Money"])
        menu()
    
    else:
        print("Code doesn't exist")
        dm()

def take_out():
    code = int(input("Code: "))
    if code == name_gp1["Code"]:
        print("£" + name_gp1["Money"])
        take = int(input("How much will you take out?: "))
        if (name_gp1["Money"] - take == name_gp1["Money"] < 0):
            print("Error 0x3867 // Cannot take enough money out!")
        else:
            print("You now have £" + str(name_gp1["Money"]) + " in the bank")
    elif code == name_gp2["Code"]:
        print("£" + name_gp2["Money"])
        
    elif code == name_gp3["Code"]:
        print("£" + name_gp3["Money"])

    
    else:
        print("Code doesn't exist")
        take_out()

#Basic menu function, uses global varible u to allow the use of a name outside a def for the welcome
def menu():
    print("Welcome " + str(u) + " to the online banking system")
    display = input("""What would you like to do today:
- Display money
- Take out money
- Deposit money
""")
    if display == "Display money" or "display money":
        dm()
    if display == "Take out money" or "take out money":
        take_out()

    else:
        menu()

#Sign up scans dicts to see if the accounts are in old dicts and if they aren't it appends it to the new dict
def sign_up():
    new_u = input("Enter new username: ")
    new_p = input("Enter new password: ")
    new_c = input("Enter new code: ")
    if new_u in name_gp1["Username"] or name_gp2["Username"]:
        print("Username exists")
        sign_up()
    if new_p in name_gp1["Password"] or name_gp2["Password"]:
        print("Password exists")
        sign_up()
    if new_c in name_gp1["Code"] or name_gp2["Code"]:
        print("Code exists")
        sign_up()    
    else:
        name_gp3["Username"].append(new_u)
        name_gp3["Password"].append(new_p)
        name_gp3["Code"].append(new_c)
        print("New Account Is Set-up")
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