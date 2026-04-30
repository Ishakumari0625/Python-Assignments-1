class bankaccount:
    def __init__(self,acc_no,initial_balance=0):
        self.acc_no=acc_no
        self.balance=initial_balance
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print("deposited succesfully")
        else:
            print("deposit amount should be +ve")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("insufficent balnce or it must be +ve")
    def check_balance(self):
        print(f"current balance: Rs{self.balance}")
account=bankaccount(1098,30000)
account.check_balance()
account.deposite(6000)
account.withdraw(400)
account.check_balance()


