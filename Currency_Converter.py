'''
Created on 7 Mar 2018

@author: obyrned1
'''

import os.path
import csv

class Currency_Converter:
    ''' all the rates and to and from euro'''
    
    def __init__(self, currencyCode, toEuroRate, fromEuroRate):
        self.currencyCode = currencyCode
        self.toEuroRate = toEuroRate
        self.fromEuroRate = fromEuroRate     
    
    def getCurrencyCode(self):
        return self.currencyCode
    
    def getToEuroRate(self):
        return self.toEuroRate
    
    def getFromEuroRate(self):
        return self.fromEuroRate
    
       
class CurrencyConvertAtlas():
    def __init__(self, csvFile):
        # this should call loadData
        self.rates = {}
        self.loadCurrencyConvert(csvFile)
        
    def loadCurrencyConvert(self, csvFile):
        with open(os.path.join(csvFile), "rt") as f:
            reader = csv.reader(f)
            for line in reader:
                self.rates[line[1]] = Currency_Converter(line[1], line[2], line[3])
        
def main():
    currency_conv = CurrencyConvertAtlas("./currencyrates.csv")
    print(currency_conv.rates['AFN'].getToEuroRate())
    
if __name__ == "__main__":
    main()
