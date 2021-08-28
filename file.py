import os

class MoneySlipsFileReader:
    BASE_PATH =  'D:/Technology/Sistemas/Gabriel/Python/PythonOOInPratice/Files'
    
    def __init__(self):
        self.__file = None
        self.__moneySlips = {}
    
    def getMoneySlips(self):
        self.__file = self.__openFileBank('r')
        line = self.__file.readline()
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
    
    def __openFileBank(self, mode):
        return open(MoneySlipsFileReader.BASE_PATH + '/_bank_file.dat', mode)
    
    def __addMoneySlipsFromFileLine(self, moneyBillValue):
        equalPosition = moneyBillValue.find('=') #2
        moneyBill = moneyBillValue[0:equalPosition] #20  
        countMoneyBillValue = len(moneyBillValue) #8
        value = moneyBillValue[equalPosition + 1:countMoneyBillValue]#80000 
        print(moneyBill, value)
        self.__moneySlips[moneyBill] = int(value)



