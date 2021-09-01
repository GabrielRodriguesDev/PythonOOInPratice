import ast
class BankFile:
    BASE_PATH =  'D:/Technology/Sistemas/Gabriel/Python/PythonOOInPratice/Files'
    
    def __init__(self):
        self._file = None
    
    def _openFileBank(self, mode):
        return open(BankFile.BASE_PATH + '/_bank_file.dat', mode)
    
    def _readlines(self):
        self._file = self._openFileBank('r')
        lines = self._file.readlines()
        self._file.close()
        return lines
    
    
    def _writeLines(self, lines):
        self._file = self._openFileBank('w')    
        self._file.writelines(lines)
        self._file.close()
    
    
    
class BankAccountFileReader(BankFile):
    
    def getLineIndexOfBankAccount(self, accountNumber):
        lines = self._readlines() #Lendo as linhas
        lines = self.__skipFirstLine(lines) #Ignorando a primeira linha
        lineIndex = -1
        for index, line in enumerate(lines):
            bankAccountCreated = self.__createBankAccountFromFileLine(line)
            if bankAccountCreated.checkAccountNumber(accountNumber):
                lineIndex = index
                break
        return lineIndex + 1

    def getAccount(self, accountNumber):
        lines = self._readlines()
        lines = self.__skipFirstLine(lines)
        bankAccount = None
        for line in lines:
            bankAccountCreated = self.__createBankAccountFromFileLine(line)
            if bankAccountCreated.checkAccountNumber(accountNumber):
                bankAccount = bankAccountCreated
                break
        return bankAccount

    def __createBankAccountFromFileLine(self, line):
        accountData = line.split(';')
        from cashMachine import BankAccount
        return BankAccount(
            accountData[0], 
            accountData[1], 
            accountData[2], 
            float(accountData[3]), 
            ast.literal_eval(accountData[4])
        )

    def __skipFirstLine(self, lines):
        return lines[1:len(lines)]
    
class BankAccountFileWriter(BankFile):
    def writeBankAccount(self, bankAccount):
        lineIndexToUpdate = BankAccountFileReader().getLineIndexOfBankAccount(bankAccount.accountNumber)
        lines = self._readlines()
        lines[lineIndexToUpdate] = self.__formatLoneToWrite(bankAccount)
        self._writeLines(lines)

    def __formatLoneToWrite(self,bankAccount):
        line ="%s;%s;%s;%s;%s;" % (
            bankAccount.accountNumber,
            bankAccount.name,
            bankAccount.password,
            str(bankAccount.value),
            str(bankAccount.admin)
        )
        return line + '\n'

class MoneySlipsFileReader(BankFile):
    
    def __init__(self):
        super().__init__() #Se referenciando ao construtor da classse pai
        self.__moneySlips = {}

    def getMoneySlips(self):
        self._file = self._openFileBank('r')
        line = self._file.readline()
        while self.__hasSemiColon(line):
            semiColonPosition = line.find(';')
            moneyBillValue = line[0:semiColonPosition]
            self.__addMoneySlipsFromFileLine(moneyBillValue)
            if self.__hasMoneyBillToRead(semiColonPosition,line):
                break
            else:
                line = line[semiColonPosition + 1:len(line)]
        return self.__moneySlips  


    def __hasMoneyBillToRead(self, semiColonPosition, line):
        return semiColonPosition + 1 == len(line) 
        
    def __hasSemiColon(self,line):
        return line.find(';') != -1 
    
    def __addMoneySlipsFromFileLine(self, moneyBillValue):
        equalPosition = moneyBillValue.find('=') #2
        moneyBill = moneyBillValue[0:equalPosition] #20  
        countMoneyBillValue = len(moneyBillValue) #8
        value = moneyBillValue[equalPosition + 1:countMoneyBillValue]#80000 
        print(moneyBill, value)
        self.__moneySlips[moneyBill] = int(value)



class MoneySlipsFileWriter(BankFile):
    def writeMoneySlips(self, moneySplips):
        lines = self._readlines()
        lines[0] = self.__formatLinesToWrite(moneySplips)
        self._writeLines(lines)

    def __formatLinesToWrite(self, moneySplips):
        line = ""
        for moneyBill, value in moneySplips.items():
            line += moneyBill + '=' + str(value) + ';'
        return line + '\n'