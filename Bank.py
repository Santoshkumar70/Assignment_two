class Bank:
    print("       Wel come    ")
    def __init__(self):
        self.pin=""
        self.changedpin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            print("Select Your Option's : ")
            print("PIN GENARATION  Enter- 1")
            # print("CHANGE YOUR PIN Enter- 2")
            print("DEPOSIT         Enter- 2")
            print("WITHDRAW        Enter- 3")
            print("CHECK BALANCE   Enter- 4")
            # print("EXIT            Enter- 6")
            user_input=input("Select Correct Option (1/2/3/4): ")
            if user_input=="1":
                self.generate_pin()
            # elif user_input =="2":
            #     self.change_pin()
            elif user_input =="2":
                self.deposit()
            elif user_input =="3":
                self.withdraw()
            elif user_input =="4":
                self.Blns_Enqury()
            else:
                print("Exit")

            

    

    def generate_pin(self):
        self.pin = int(input("Enter Pin"))
        print("PIN GENERATION SUCESSFULLY.....")

    # def change_pin(self):
    #     old_pin = int(input("Enter Your old pin : "))
    #     if old_pin == self.pin:
    #         self.changedpin = int(input("Enter New pin : "))
    #         print("Pin Changed Sucessfully....")
    #     else:
    #         print("Invalid pin...")

    def deposit(self):
        pin = int(input("Enter Your pin..."))
        if pin == self.pin:
            amount = int(input("Enter Deposit Amount : "))
            self.balance += amount
            print("Congrulations ",self.balance," Depoisted in Your Account..")
            print("Thank You for Using Santosh Kumar Bank.. ")
            print("Visit Again")
        else:
            print("In correct pin")
        
    def withdraw(self):
        pin = input("Enter Your pin...")
        if pin == self.pin :
            amount = int(input("Enter Amount..."))
            if amount < self.balance:
                self.balance -= amount
                print(amount,"Withdraw sucessfully in Your Account....")
            else:
                print("Innsufficent Balance... ")
        else:
            print("Invalid Pin...")
    
    def Blns_Enqury(self):
        pin = int(input("Enter Your pin..."))
        if pin == self.pin :
            print("Your Account Balance is : ",self.balance)
        else:
            print("Invalid pin...")
        

Bank()
        