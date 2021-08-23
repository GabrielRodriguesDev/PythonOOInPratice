from cashMachine import accountList

class AuthBankAccount:
    bankAccountAuthenticated = None # DICA: Variavel estatica, assim pode acessar a variavel, acessando a classe não necessáriamente precisa pegar a referencia do objeto instanciado, só acessa  classe.
    
    @staticmethod
    def authenticate(accountNumber, password):
        for bankAccount in accountList:
            if AuthBankAccount.hasBankAccountValid(bankAccount, accountNumber, password):
                AuthBankAccount.bankAccountAuthenticated = bankAccount
                return bankAccount
        return False
    
    @staticmethod
    def hasBankAccountValid(bankAccount, accountNumber, password):
        return bankAccount.checkAccountNumber(accountNumber) and \
                bankAccount.checkPassword(password)

