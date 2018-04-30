'''
Created on 7 Mar 2018

@author: obyrned1
'''

from Airport import *
 
airportDict = AirportAtlas("./airport.csv")
currencyDict = CurrencyAtlas("./currencyrates.csv", "./countrycurrency.csv")
   
airCode1 = 'HEA'
airCode2 = 'DUB'
# test the methods in the AirportAtlas class
def testLoadData():
    '''test to assert the code dictionary is populated and info can be accessed using getter methods'''
    assert airportDict.codes[airCode1].getCountry() == 'Afghanistan'
           
def testGreatCircledlist():
    '''test to assert the GreatCircleList is working'''
    lat1 = airportDict.codes[airCode1].getLat()
    lat2 = airportDict.codes[airCode2].getLat()
    long1 = airportDict.codes[airCode1].getLong()
    long2 = airportDict.codes[airCode2].getLong()
    assert  float('%.1f'%(airportDict.greatCircledlist(lat1, long1, lat2, long2))) == 5647.9
    # hard-coded value of 5647.9 was retrieved from google
    
def testgetDistanceBetweenAirports():
    '''test to assert distanceBetweenAirports is working'''
    assert float('%.1f'%(airportDict.getDistanceBetweenAirports(airCode1, airCode2))) == 5647.9
    # hard-coded value of 484.5 was retrieved from google

def testCostOfTrip():
    '''test to assert the cost of a single leg of a journey'''
    distance = float('%.1f'%(airportDict.getDistanceBetweenAirports('DUB','LGW')))
    countryName = airportDict.codes[airCode2].getCountry()
    euroRate = currencyDict.currencies[countryName].getToEuroRate()
    assert airportDict.costOfTrip(euroRate, distance) == 484.50

def testPossibleCombinations():
    '''test to assert the combinations function creates a dictionary, where the keys are possible second stops 
    on a route. The values are then all possible combinations of the route where the key is the second stop'''
    route = ['AAH', 'SVX', 'IBE', 'KON']
    dict = airportDict.possibleCombinations(airCode1, route)
    assert dict['AAH'][1][0] == 'AAH'
    # this checks the second value in the dictionary is the same as the key


    
    