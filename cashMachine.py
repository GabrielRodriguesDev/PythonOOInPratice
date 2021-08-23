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
        
        
accountList = [
    BankAccount('0001-02', 'Gabriel Silva', '123456', 100, True),
    BankAccount('0002-02', 'Andre Silva', '123456', 1000, False)
]

