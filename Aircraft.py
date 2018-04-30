'''
Created on 22 Apr 2018

@author: obyrned1
'''
import os.path
import csv
from scipy.constants.codata import unit

class Aircraft:
    ''' Loads in the aircraft data and extracts relevant information'''
    
    def __init__(self, aircraftCode, units, craftRange):
        self.aircraftCode = aircraftCode
        self.craftRange = craftRange
        self.units = units
        
    def getCode(self):
        return self.aircraftCode
    
    def getRange(self):
        '''returns the range of an aircraft'''
        if self.units == 'imperial':
            aircraftRange = float(self.craftRange)
            aRange = aircraftRange*1.609344
        else:
            aRange = float(self.craftRange)
            
        return aRange
    
class AircraftAtlas:
    
    aircrafts = {}
    
    def __init__(self, csvFile):
        self.loadAircrafts(csvFile)
        
    def loadAircrafts(self, csvFile):
        '''creates a dictionary with relevant information from given csvFile'''
        with open(os.path.join(csvFile), "rt") as f:
            reader = csv.reader(f)
            for line in reader:
                self.aircrafts[line[0]] = Aircraft(line[0], line[2], line[4])
                