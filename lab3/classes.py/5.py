class Account():
    def __init__(self, owner:str, balance=0):
        self.owner=owner
        self.balance=balance
        
    def dep(self, add):
        self.balance=self.balance + add
    def withdr(self,withdraw):
        if(self.balance - withdraw >= 0):
            self.balance = self.balance - withdraw
            print("money withdrawn")
            print('on card: ' + str(self.balance))
        else:
            print('not enough money')
    def info(self):
        print('name: ' + self.owner)
        print('balance: ' + str(self.balance))

p = Account('Yerkenaz', 300)
p.dep(200)
p.withdr(600)
p.info() 