class BankAccount:
    def __init__( self, accountNumber, name, password, value, admin ):
        self.accountNumber = accountNumber
        self.name = name
        self.password = password
        self.value = value
        self.admin = admin
        
    def checkAccountNumber(self, accountNumber):
        return self.accountNumber == accountNumber
    
    def checkPassword(self, password):
        return self.password == password
    
    def balanceDebit(self, value):
        self.value -= value
        
class CashMachineWithdraw:
    
    @staticmethod
    def withdraw(bankAccount, value):
        cashMachine = CashMachine(
            {
                '20': 5,
                '50': 5,
                '100': 5,
            }
        )
        money_slips_user = cashMachine.withdraw(value)
        if money_slips_user:
            bankAccount.balanceDebit(value)
        return cashMachine
        
        
class CashMachine:
    def __init__(self, moneySlips):
        self.moneySlips  = moneySlips
        self.moneySplipsUser = {}
        self.valueRemainig = 0
        
    def withdraw(self, value):
        self.valueRemainig = value
        
        self.__calculateMoneySlipsUser('100')
        self.__calculateMoneySlipsUser('50')
        self.__calculateMoneySlipsUser('20')
        
        if self.valueRemainig == 0:
            self.__decreaseMoneySlips()
        
        return False if self.valueRemainig != 0 else self.moneySlips
            
    def __calculateMoneySlipsUser(self, moneyBill):
        moneyBillInt = int(moneyBill)
        if self.valueRemainig // moneyBillInt > 0 and self.valueRemainig // moneyBillInt <= self.moneySlips[
            moneyBill]:
            self.moneySplipsUser[moneyBill] = self.valueRemainig // moneyBillInt
            self.valueRemainig = (self.valueRemainig - ((self.valueRemainig // moneyBillInt) * moneyBillInt))
            
    def __decreaseMoneySlips(self):
        for moneyBill in self.moneySplipsUser:
            #moneyBillStr = str(moneyBill)
            self.moneySlips[moneyBill] -= self.moneySplipsUser[moneyBill]
            #print(self.moneySlips[moneyBillStr])
            #print(self.moneySplipsUser[moneyBillStr])
            
        

accountList = [
    BankAccount('0001-02', 'Gabriel Silva', '123456', 100, True),
    BankAccount('0002-02', 'Andre Silva', '123456', 1000, False)
]



