'''
Created on 7 Mar 2018

@author: obyrned1
'''

from Currency import *
from collections import deque
import csv

file1 = "./currencyrates.csv"
file2 = "./countrycurrency.csv"
currencyDict = CurrencyAtlas(file1, file2)

def testJoinCsv():
    '''test to assert if the join csv function is working correctly, by testing its output, mergedCurrency.csv'''
    with open('./mergedCurrency.csv', 'r') as f:
        lastrow = deque(csv.reader(f), 1)[0]
    assert lastrow == ['243', 'Zimbabwe Dollar', 'ZWD', '0.002542', '396.647', 'Zimbabwe']
    # the merged CSV should be in alphabetical order by currency name. 
    # Zimbabwe Dollar should be the last on this list and Zimbabwe is the only country to use it
    
def testLoadData():
    '''test to assert the currencies dictionary is populated and info can be accessed using getter methods'''
    assert currencyDict.currencies['Zimbabwe'].getToEuroRate() == '0.002542'
   
    
