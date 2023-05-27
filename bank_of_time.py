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
    if u in name_gp1["Username"] and p in name_gp1["Password"]:
        print("\\\\\ Log-In Successful /////")
        menu()
    elif u in name_gp2["Username"] and p in name_gp2["Password"]:
        print("\\\\\ Log-In Successful /////")
        menu()
    elif u in name_gp3["Username"] and p in name_gp3["Password"]:
        print("\\\\\ Log-In Successful /////")
        menu()
    
    else:
        print("Credentials Incorrect")
        log_in()

#Display Money or dm scans the dicts to look for the code and then outputs the money in the account
def dm():
    code = int(input("Code: "))
    if code == name_gp1["Code"]:
        print("£" + str(name_gp1["Money"]))
        menu()
    elif code == name_gp2["Code"]:
        print("£" + str(name_gp2["Money"]))
        menu()
    elif code == name_gp3["Code"]:
        print("£" + str(name_gp3["Money"]))
        menu()
    
    else:
        print("Code doesn't exist")
        dm()

#Take out scans for the correct code and then allows the user to take out money that is less or equal to what's in their bank
def take_out():
    global u
    code = int(input("Code: "))
    if code == name_gp1["Code"] and u in name_gp1["Username"]:
        print("You have £"+ str(name_gp1["Money"]) +" in the bank")
        take = int(input("How much will you take out?: "))
        if take > name_gp1["Money"]:
            print("Error 0x3867 // Not Enough In Bank!")
            take_out()
        else:
            name_gp1["Money"] = name_gp1["Money"] - take
            print("You now have £" + str(name_gp1["Money"]) + " in the bank")
            menu()
    
    elif code == name_gp2["Code"] and u in name_gp2["Username"]:
        print("You have £"+ str(name_gp2["Money"]) +" in the bank")
        take = int(input("How much will you take out?: "))
        if take > name_gp2["Money"]:
            print("Error 0x3867 // Not Enough In Bank!")
            take_out()
        else:
            name_gp2["Money"] = name_gp2["Money"] - take
            print("You now have £" + str(name_gp2["Money"]) + " in the bank")
            menu()
        
    elif code == name_gp3["Code"] and u in name_gp3["Username"]:
        print("You have £"+ str(name_gp3["Money"]) +" in the bank")
        take = int(input("How much will you take out?: "))
        if take > name_gp1["Money"]:
            print("Error 0x3867 // Not Enough In Bank!")
            take_out()
        else:
            name_gp1["Money"] = name_gp1["Money"] - take
            print("You now have £" + str(name_gp1["Money"]) + " in the bank")
            menu()

    else:
        print("Code is wrong or doesn't exist")
        take_out()

def deposit():
    code = int(input("Code: "))
    if code == name_gp1["Code"]:
        print("You have £"+ str(name_gp1["Money"]) +" in the bank")
        add = int(input("How much will you put in?: "))
        if add == 0:
            print("Please enter a bigger value")
            deposit()
        else:
            name_gp1["Money"] = name_gp1["Money"] + add
            print("You now have £" + str(name_gp1["Money"]) + " in the bank")
            menu()
    
    elif code == name_gp2["Code"]:
        print("You have £"+ str(name_gp2["Money"]) +" in the bank")
        add = int(input("How much will you put in?: "))
        if add == 0:
            print("Please enter a bigger value")
            deposit()
        else:
            name_gp2["Money"] = name_gp2["Money"] + add
            print("You now have £" + str(name_gp2["Money"]) + " in the bank")
            menu()
        
    elif code == name_gp3["Code"]:
        print("You have £"+ str(name_gp3["Money"]) +" in the bank")
        add = int(input("How much will you take out?: "))
        if add == 0:
            print("Error 0x3867 // Not Enough In Bank!")
            deposit()
        else:
            name_gp1["Money"] = name_gp1["Money"] + add
            print("You now have £" + str(name_gp1["Money"]) + " in the bank")
            menu()

    else:
        print("Code doesn't exist")
        take_out()

#Basic menu function, uses global varible u to allow the use of a name outside a def for the welcome
def menu():
    print("Welcome " + str(u) + " to the online banking system")
    display = int(input("""What would you like to do today:
1 - Display money
2 - Take out money
3 - Deposit money
4 - Log-in
5 - Quit
"""))
    if display == 1:
        dm()
    if display == 2:
        take_out()
    if display == 3:
        deposit()
    if display == 4:
        log_in()
    if display == 5:
        quit()

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
    1 - Login
    2 - Sign Up
    3 - Quit
    """))
    if option == 1:
        log_in()
    if option == 2:
        sign_up()
    if option == 3:
        quit()

print("Bank Version 1.4")
options()