#Bank account simple system
class Bank_Account:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name
    def deposite(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance +=amount
        print("\n Amount deposited: ", amount)
        
    def  withdraw(self):
        amount=float(input("Enter amount to be withdrawn: "))
        if(amount>self.balance):
            print("You have insufficient funds")
        else:
            self.balance-=amount
            print("\n You withdrew:", amount) 
            
    def check_balance(self):
        print("\n Your remaining balance is: ", self.balance)
        
    def customer_details(self):
        print("Account number: ", self.account_number)
        print("Balance: ", self.balance)
        print("Date of opening: ",self.date_of_opening)
        print("Customer name: ",self.customer_name)
    
ba=Bank_Account(account_number=1530181159402,
                balance=0,
                date_of_opening=("12th of march year 2009"),
                customer_name=("Moses Omondi"))
print(ba.deposite())
print(ba.withdraw())
print(ba.check_balance())
print(ba.customer_details())