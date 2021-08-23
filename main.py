from console import AuthBankAccountConsole, CashMachineConsole
from utils import clear, header

def main():
    clear()
    header()
    if AuthBankAccountConsole.isAuth():
        clear()
        header()
        CashMachineConsole.callOperation()
    else:
        print('Conta inválida')
        
if __name__ == '__main__':
    while True:
        main()
        input('Pressione <ENTER> para continuar...')
        