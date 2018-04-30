'''
Created on 7 Mar 2018

@author: obyrned1
'''
import os.path
import csv
import pandas as pd

class Currency:
    '''country name and code. source currency and destination currency'''
    
    def __init__(self, countryName, currencyName, toEuroRate):
        self.currencyName = currencyName
        self.toEuroRate = toEuroRate
        self.countryName = countryName
              
    def getCountryName(self):
        return self.countryName
    
    def getCurrencyName(self):
        return self.currencyName
      
    def getToEuroRate(self):
        return self.toEuroRate
       
class CurrencyAtlas:
    
    currencies={}
    
    def __init__(self, csvFile1, csvFile2):
        self.joinCsv(csvFile1, csvFile2)
        
    def joinCsv(self, csvFile1, csvFile2):
        '''joins the two csv files provided to extract only the relevant information'''
        df1 = pd.read_csv(csvFile1, header=None)
        currencyCode = df1[1] 
        toEuroRate = df1[2] 
        fromEuroRate = df1[3]
        df1.columns = ['currency_name', 'currency_alphabetic_code', 'toEuroRate','fromEuroRate']
        df2 = pd.read_csv(csvFile2)
        df3 = df2[['currency_alphabetic_code', 'name']]
        currencyCode1 = df3['currency_alphabetic_code']
        currencyCountry = df3['name']
        df4 = pd.merge(df1, df3, on='currency_alphabetic_code')
        df4.dropna()
        df4.to_csv("./mergedCurrency.csv")
        self.loadCurrencyData("./mergedCurrency.csv")
        
    def loadCurrencyData(self, csvFile):
        '''creates a dictionary with relevant information from given csvFile'''
        with open(os.path.join(csvFile), "rt") as f:
            reader = csv.reader(f)
            for line in reader:
                self.currencies[line[5]] = Currency(line[5], line[1], line[3])
                # (5)name = (5)name, (1)currency_name, (3)to_euro

    