#List of dictionaries with users log-in info
users = {
    "Username": ["Pix", "Jin"], 
    "Password": ["jUmP?", "tOy!"],
    "Money": [120, 58],
    "Code": [2385, 6785 ]
}

u = ""
value = 0

#The basic log-in feature which scans the dicts to see if the username and passwords are there.
def log_in():
    global u
    global u_i
    global value
    u = input("Username: ")
    p = input("Password: ")
    u_i = [index for (index, item) in enumerate(users["Username"])if item == u]
    p_i = [index for (index, item) in enumerate(users["Password"])if item == p]
    m_i = [index for (index, item) in enumerate(users["Money"])if item == u]
    for m_i in range(len(users["Money"])):
        value = users["Money"][m_i]
    if u_i == p_i and u and p != "":
        print("\\\\\ Log-In Successful /////")
        menu()
    else:
        print("Credentials Incorrect")
        log_in()

#Display Money or dm scans the dicts to look for the code and then outputs the money in the account
def dm():
    global value
    code = int(input("Code: "))
    c_i = [index for (index, item) in enumerate(users["Code"])if item == code]
    if (u_i == c_i):
        for m_i in range(len(users["Money"])):
            if value != users["Money"][m_i]:
                print("£%s\n" % str(value))
                menu()
            else:    
                value = users["Money"][m_i]
                print("£%s\n" % str(value)) 
                menu()
    else:
        print("Code doesn't exist")
        dm()

#Take out scans for the correct code and then allows the user to take out money that is less or equal to what's in their bank
def take_out():
    code = int(input("Code: "))
    c_i = [index for (index, item) in enumerate(users["Code"])if item == code]
    if (u_i == c_i):
        for m_i in range(len(users["Money"])):
                if value == users["Money"][m_i]:
                    print("You have £"+ str(value) +" in the bank")
                    take = int(input("How much will you take out?: "))
                    if take > value:
                        print("Error 0x3867 // Not Enough In Bank!")
                        take_out()
                    else:
                        value -= take
                        print("You now have £" + str(value) + " in the bank\n")
                        menu()
                elif value < users["Money"][m_i] or value > users["Money"][m_i]:
                    print("You have £"+ str(value) +" in the bank")
                    take = int(input("How much will you take out?: "))
                    if take > value:
                        print("Error 0x3867 // Not Enough In Bank!")
                        take_out()
                    else:
                        value -= take
                        print("You now have £" + str(value) + " in the bank\n")
                        menu()
                else:
                    take_out()
    else:
        print("Code is wrong or doesn't exist")
        take_out()

def deposit():
    global value
    code = int(input("Code: "))
    c_i = [index for (index, item) in enumerate(users["Code"])if item == code]
    m_i = [index for (index, item) in enumerate(users["Money"])if item == code]
    if (u_i == c_i):
        for m_i in range(len(users["Money"])):
            value = users["Money"][m_i]
            print("You have £"+ str(value) +" in the bank")
            add = int(input("How much will you put in?: "))
            if add == 0:
                print("Please enter a bigger value")
                deposit()
            else:
                value += add
                print("You now have £" + str(value) + " in the bank\n")
                menu()

    else:
        print("Code doesn't exist")
        take_out()

def mort_cal():
    loanAmount = float(input("Enter loan amount: "))

    years = float(input("Years to have the loan: ")) * 12
    
    interestRate = float(input("Enter Interest Rate: ")) / 100 / 12

    mortgagePayment = loanAmount * (interestRate * (1 + interestRate) \
                                    ** years) / ((1 + interestRate) ** years - 1)
    
    print("The monthly mortgage payment is £%.2f" % mortgagePayment)

#Basic menu function, uses global varible u to allow the use of a name outside a def for the welcome
def menu():
    print("Welcome " + str(u) + " to the online banking system")
    display = int(input("""What would you like to do today:
1 - Display money
2 - Take out money
3 - Deposit money
4 - Mortgage Calculator
5 - Log-in
6 - Quit
"""))
    if display == 1:
        dm()
    if display == 2:
        take_out()
    if display == 3:
        deposit()
    if display == 4:
        mort_cal()
    if display == 5:
        log_in()
    if display == 6:
        quit()

    else:
        menu()

#Sign up scans dicts to see if the accounts are in old dicts and if they aren't it appends it to the new dict
def sign_up():
    new_u = input("Enter new username: ")
    new_p = input("Enter new password: ")
    new_c = int(input("Enter new code: "))
    if new_u in users["Username"]:
        print("Username exists")
        sign_up()
    if new_p in users["Password"]:
        print("Password exists")
        sign_up()
    if new_c == users["Code"]:
        print("Code exists")
        sign_up()    
    else:
        users["Username"].append(new_u)
        users["Password"].append(new_p)
        users["Code"].append(new_c)
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