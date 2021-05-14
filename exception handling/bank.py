class Bank:
    bname="sbi"
    def account(self,acno,name#bname):
        #self.bname=bname
        self.acno=acno
        self.name=name
        self.minimumbal=5000
        self.balance=self.minimumbal
    def deposit(self,amt):
        self.balance+=amt
        print("your acc balance has been credited with amt",amt)
    def withdraw(self,amt):
        if amt>self.balance:
            print("insufficient balance")
        else:
            print("acc debited with",amt)
            self.balance-=amt
            print("available balance",self.balance)
obj=Bank()
obj.account(133,'abc'#'sbi')
obj.deposit(2500)
obj.withdraw(1500)