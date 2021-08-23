class CashMachineConsole: #DICA: Abstraia o código em classes para que fique facil o entendimento.
#DICA: Matenha a ordem de leitura do código linear, portanto a função principal em cima e abaixo as que serão chamadas pela principal, e assim por diante... O mesmo vale para as classes.    
    
    @staticmethod # DICA: Métodos estáticos devem ser usados quando o método não vai receber ou gerenciar  "nenhum atributo da classe", apenas processar alguma logica
    def callOperation():
        optionTyped = CashMachineConsole.getMenuOptionsTyped()
        CashMachinheOperation.doOperation(optionTyped)
    
    @staticmethod
    def getMenuOptionsTyped():
        print("1 - Saldo")
        print("2 - Saque")
        return input('Escolha uma das opções acima: ')
    


class CashMachinheOperation:       
    
    @staticmethod
    def doOperation(option):
        if option == '1':
            ShowBalanceOperation.doOperation()
        elif option == '2':
            WithDrawOperation.doOperation()
        
        
class ShowBalanceOperation:
    
    @staticmethod
    def doOperation():
        print('Mostrar Saldo')

class WithDrawOperation:
    
    @staticmethod
    def doOperation():
        print('Sacar dinheiro')