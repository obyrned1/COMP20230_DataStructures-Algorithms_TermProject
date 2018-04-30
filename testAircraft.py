'''
Created on 7 Mar 2018

@author: obyrned1
'''

from Aircraft import *

aircraftDict = AircraftAtlas("./aircraft.csv")

def testLoadAircrafts():
    '''test to assert the aircraft dictionary is populated and info can be accessed using getter methods'''
    assert aircraftDict.aircrafts['747'].getCode() == '747'
    # the aircrafts dictionary has a key of the craft code, and values of this code and the range
    
def testGetRange():
    '''test to assert the aircraft dictionary has populated the range properly, changing to km if imperial'''
    assert float('%.1f'%(aircraftDict.aircrafts['747'].getRange())) == 15771.6
    # the range for a 747 is given in imperail as 9800, converted to km its 15771.6