class Account: #There isn't a warning "Class names should use CamelCase convention, why?"
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print("account created for "+self.name)

    def deposit(self,amount):
        if amount >0:
            self.balance += amount
        #show_balance()#NameError: name 'show_balance' is not defined
        self.show_balance()
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance -= amount
        else:
            print("the amount should between 0 and balance")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self.balance))

if __name__ == '__main__': #定义main函数，注意是两个等号
    tim = Account("tim",0)
    tim.deposit(500)
    tim.withdraw(1000)


#创建1个实例时，1.调用__new__创建该实例，一般不常用
# 2.用__init__为实例赋值 3
/Users/rose/Downloads/programming/python-masterclass
/Users/rose/Downloads/programming/python-masterclass/.idea/dictionaries/account.py