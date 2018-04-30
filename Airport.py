'''
Created on 7 Mar 2018

@author: obyrned1
'''

import os.path
import csv
from math import pi,sin,cos,acos
import pandas as pd
import itertools

from Currency import CurrencyAtlas 
from Aircraft import AircraftAtlas


class Airport():
    '''name, lat, long, code, maybe other attributes'''   
    
    def __init__(self, code, country, airportName, airportLat, airportLong ):
        # the 5th column in the csv is the three letter airport code, index 4
        self.code = code
        self.country = country
        self.airportName = airportName
        self.airportLat = airportLat
        self.airportLong = airportLong   
    
    def getCode(self):
        return self.code

    def getCountry(self):
        return self.country
    
    def getName(self):
        return self.airportName
    
    def getLat(self):
        return float(self.airportLat)
    
    def getLong(self):
        return float(self.airportLong) 
       
class AirportAtlas():
    def __init__(self, csvFile):
        # this should call loadData
        self.codes={}
        self.loadData(csvFile)
        
    def loadData(self, csvFile):
        '''creates a dictionary with relevant information from given csvFile'''
        with open(os.path.join(csvFile), "rt") as f:
            reader = csv.reader(f)
            for line in reader:
                self.codes[line[4]] = Airport(line[4], line[3], line[1], line[6], line[7])
        
    def getAirport(self, code):
        '''returns the code for an airport'''
        return self.codes[code]
        
    def greatCircledlist(self, lat1, long1, lat2, long2):
        '''takes two lats and longs and gets the great circle distance between them'''
        radius_earth = 6371 #km
        theta1 = long1 * (2 * pi) / 360
        theta2 = long2 * (2 * pi) /360
        phi1 = (90 - lat1) * (2 * pi) /360
        phi2 = (90 - lat2) * (2 * pi) /360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * radius_earth
        return distance
    
    def getDistanceBetweenAirports(self,code1,code2):
        '''this method has to read two 3 digit codes, get the corresponding long and lat, then call the distanceBetweenPoints'''
        airA = self.getAirport(code1)
        lat1 = airA.getLat()
        long1 = airA.getLong()
        airB = self.getAirport(code2)
        lat2 = airB.getLat()
        long2 = airB.getLong()
        return self.greatCircledlist(lat1, long1, lat2, long2)
    
    def costOfTrip(self, rate, distance):
        '''calculate the cost of a single leg of a journey'''
        cost1 = float(rate) * float(distance)
        cost2 = float("{0:.2f}".format(cost1))
        return cost2
    
    def possibleCombinations(self, home, route):
        '''returns a dictionary will all possible route combinations'''
        # comboKeys is a dictionary that will hold all possible combinations of routes, where the key 
        # is one of the 4 possible 2nd stop options, and the values are possible combinations, which all 
        # start with the key (possible 2nd stop)
        comboKeys = {}
        
        #comboValues is an array that will hold these possible combinations
        comboValues = []

        count = 0

        for each in itertools.permutations(route):
            comboValues.append(home)
            comboValues.append(each)
            comboValues.append(home)
            count += 1
            
            # there are six possible combinations of the 4 stops, starting with each possible 2nd stop 
            # when it's reached 6, clear the array (comboValues), reset count, and start fresh with a new 2nd stop 
            if count == 6:
                # set the value as the comboValues array, where the key is the 2nd stop option
                comboKeys[each[0]] = comboValues
                count = 0
                comboValues = []
                
        return comboKeys
    
    
        
    





