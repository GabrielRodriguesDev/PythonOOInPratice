
from cashMachine import CashMachineInsertMoneyBill, CashMachineWithdraw
from auth import AuthBankAccount
import socket



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
        bankAccount = AuthBankAccount.bankAccountAuthenticated
        if bankAccount.admin:
            print(CashMachinheOperation.OPERATIONINSERTMONEYBILL + " - Inserir cédulas")
        return input('Escolha uma das opções acima: ')

class CashMachinheOperation:       
    OPERATIONSHOWBALANCE = '1'
    OPERATIONWITHDRAW = '2'
    OPERATIONINSERTMONEYBILL = '10'
    
    @staticmethod
    def doOperation(option):
        bankAccount = AuthBankAccount.bankAccountAuthenticated
        if option == CashMachinheOperation.OPERATIONSHOWBALANCE:
            ShowBalanceOperation.doOperation()
        elif option == CashMachinheOperation.OPERATIONWITHDRAW:
            WithDrawOperation.doOperation()
        elif option == CashMachinheOperation.OPERATIONINSERTMONEYBILL and bankAccount.admin:
            InsertMoneyBillOperation.doOperation()
        else:
            print('Opção inválida')
            

        
        
class ShowBalanceOperation:
    
    @staticmethod
    def doOperation():
        banckAccount = AuthBankAccount.bankAccountAuthenticated
        print('Seu saldo é %s' % banckAccount.value) # Mostrando valor sem ser por concatenação, forma parecida com a do C
        

class WithDrawOperation:
    
    @staticmethod
    def doOperation():
        valueTyped = input("Digite o valor a ser sacado: ")
        valueInt =  int(valueTyped)
        bankAccount = AuthBankAccount.bankAccountAuthenticated
        cashMachine = CashMachineWithdraw.withdraw(bankAccount,valueInt)
        if cashMachine.valueRemainig != 0:
            print("O caixa não tem cédulas disponveis para este valor")
        else:
            print("Pegue as notas")
            print(cashMachine.moneySplipsUser)
            print(vars(bankAccount))

class InsertMoneyBillOperation:
    def doOperation():
        amountTyped = input('Digite a quantidade de cédulas: ')
        moneyBillTyped = input('Digite a cédula a ser incluída: ')
        cashMachine = CashMachineInsertMoneyBill.insertMoneyBill(moneyBillTyped, int(amountTyped))
        print(cashMachine.moneySlips)