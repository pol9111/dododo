class Account:

    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("The amount of the deposit shall not be nagative.")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount >= self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount

    def desc(self):
        return print("Account({name}, {number}, {balacne})".format(name=self.name, number=self.number, balacne=self.balance))


User1 = Account(name='Trleo', number=6217, balance=0)
User1.deposit(8888)
User1.withdraw(888)
User1.desc()









