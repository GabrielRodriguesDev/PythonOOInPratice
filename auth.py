from file import BankAccountFileReader
from cashMachine import accountList

class AuthBankAccount:
    bankAccountAuthenticated = None # DICA: Variavel estatica, assim pode acessar a variavel, acessando a classe não necessáriamente precisa pegar a referencia do objeto instanciado, só acessa  classe.
    
    @staticmethod
    def authenticate(accountNumber, password):
        bankAccountFr = BankAccountFileReader()
        bankAccount = bankAccountFr.getAccount(accountNumber)
        if bankAccount and  AuthBankAccount.__hasBankAccountValid(bankAccount, accountNumber, password):
            AuthBankAccount.bankAccountAuthenticated = bankAccount
            return bankAccount
        return False
    
    @staticmethod
    def __hasBankAccountValid(bankAccount, accountNumber, password): #Dois anderline antes de método ou variavel o torna privado (Acessivel apenas para a própria classe)
        return bankAccount.checkAccountNumber(accountNumber) and \
                bankAccount.checkPassword(password)

