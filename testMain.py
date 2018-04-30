'''
Created on 7 Mar 2018

@author: obyrned1
'''
from main import *
from Airport import *
from Aircraft import *
from Currency import *

airportDict = AirportAtlas("./airport.csv")
currencyDict = CurrencyAtlas("./currencyrates.csv", "./countrycurrency.csv")
aircraftDict = AircraftAtlas("./aircraft.csv")

def testMain():
    '''test to assert that the main method correctly calculates the cheapest route, if feasible'''
    data = main('./testMainRoute.csv', airportDict, currencyDict, aircraftDict)
    # I have created a testMainRoute.csv with only one line in it which is an input example from Khalil's(TA) file
    # The main function returns data, which is the line to populate the bestroutes.csv
    # testing to see whether data matches the correct output as given by Khalil(TA)
    assert data == '747,  LOV    BBO    BHI    VKO    VCS  ,  LOV -->  VKO -->  VCS -->  BBO -->  BHI -->  LOV  ,Feasible,1658.62'
    



