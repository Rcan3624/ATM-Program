Note: This is still a work in progress

# Ryan Cannon

# This is a port of my ATM Flowchart project



def InitalizeAccounts():
    CustomerName = ["Robert Brown", "Lisa White", "Mark Black", "Ryan Cannon"]
    UsernameStorage = ["rbrown", "lwhite", "mblack", "Rcannon13@ivytech.edu"]
    PasswordStorage = ["blue123", "red456", "green789", "C04691798"]
    CheckingBalance = [35, 1250, 200, 900]
    SavingsBalance = [2500, 500, 750, 600]


def Login():
    print("Welcome")
    print("Please note that this ATM does not accept decimal values and will not dispense change.")
    Username = input("Enter username: ")
    while Attempt >=3:

    pass

def Password():
    pass

def Options():
    pass

def UsernameStringCheck():
    pass

def PasswordStringCheck():
    pass

def MenuNumberCheck():
    pass

def RemovalDecimal():
    pass

def Deposit():
    pass

def Withdraw():
    pass

def Balance():
    pass

def Transfer():
    pass

def CheckIfDepositValid():
    pass

def Checking_Overdraft_Prevention():
    pass

def Savings_Overdraft_Prevention():
    pass

def main():
    print("Staring up system")
    print("Loading Variables...")
    Transaction = 0
    TransactionCount = 0
    MenuChoice = 0
    Attempt = 0
    Username = ""
    Password = ""
    Index = 1
    print("Variables loaded")
    InitalizeAccounts()
    print("Startup complete")
    Login()
    print("Goodbye")





main()