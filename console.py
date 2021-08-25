
from auth import AuthBankAccount


class AuthBankAccountConsole:
    
    @staticmethod
    def isAuth():
        accountNumberTyped = input('Digite sua conta: ')
        passwordTyped = input('Digite sua senha: ')
        return AuthBankAccount.authenticate(accountNumberTyped, passwordTyped)

class CashMachineConsole: #DICA: Abstraia o código em classes para que fique facil o entendimento.
#DICA: Matenha a ordem de leitura do código linear, portanto a função principal em cima e abaixo as que serão chamadas pela principal, e assim por diante... O mesmo vale para as classes.    
    
    @staticmethod # DICA: Métodos estáticos devem ser usados quando o método não vai receber ou gerenciar  "nenhum atributo da classe", apenas processar alguma logica
    def callOperation():
        optionTyped = CashMachineConsole.__getMenuOptionsTyped()
        CashMachinheOperation.doOperation(optionTyped)
    
    @staticmethod
    def __getMenuOptionsTyped():
        print(CashMachinheOperation.OPERATIONSHOWBALANCE + " - Saldo")
        print(CashMachinheOperation.OPERATIONWITHDRAW + " - Saque")
        return input('Escolha uma das opções acima: ')

class CashMachinheOperation:       
    OPERATIONSHOWBALANCE = '1'
    OPERATIONWITHDRAW = '2'
    
    @staticmethod
    def doOperation(option):
        if option == CashMachinheOperation.OPERATIONSHOWBALANCE:
            ShowBalanceOperation.doOperation()
        elif option == CashMachinheOperation.OPERATIONWITHDRAW:
            WithDrawOperation.doOperation()
        
        
class ShowBalanceOperation:
    
    @staticmethod
    def doOperation():
        print('Mostrar Saldo')
        print(AuthBankAccount.bankAccountAuthenticated)

class WithDrawOperation:
    
    @staticmethod
    def doOperation():
        print('Sacar dinheiro')