class Banking:
    def __init__(self, Deposited):
        self.Deposited=Deposited
    def Deposit(self,deposit):
        self.Deposited+=deposit
    def Withdraw(self,Withdraw):
        if(Withdraw<= self.Deposited):
            self.Deposited-=Withdraw
        else:
            print("insufficient balance")
    def Display(self):
        print("Balance: ",self.Deposited) 
p1 = Banking(5000)

p1.Display()

p1.Deposit(4000)
p1.Display()

p1.Withdraw(3000)
p1.Display()

p1.Withdraw(10000)
p1.Display()