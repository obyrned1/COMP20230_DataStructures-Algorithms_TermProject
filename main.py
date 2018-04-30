'''
Created on 7 Mar 2018

@author: obyrned1
'''
import os.path
import csv
import itertools
import queue

from Airport import AirportAtlas
from Currency import CurrencyAtlas 
from Aircraft import AircraftAtlas
from asyncio.queues import Queue


def writeHeader():
    header = 'Aircrafts' + ',' + 'Airports' + ',' + 'Cheapest Path' + ',' + 'Feasibility' + ',' + 'Fuel Cost'
    with open('bestroutes.csv','a') as file:
        file.write(header)
        file.write('\n')
                
def feasibleToCsv(cheapRoute, cheapestCost, aircraft, routeStops, stops):
    
    bestRoute = str(cheapRoute)
    routeCost = str(cheapestCost)
                
    for ch in ['[', ']', '\'']:
        if ch in bestRoute:
            bestRoute = bestRoute.replace(ch," ")
    bestRoute = bestRoute.replace(",","-->")
    for ch in ['[', ']', '\'', ',']:
        if ch in routeCost:
            routeCost = routeCost.replace(ch," ")

    feasibleRoute = "Feasible"
    
    print("Route stops:", stops)
    print("The cheapest route is:", cheapRoute,". Which costs: E", cheapestCost)
    print("-------------------------------------------------------------------------------------------------") 
    data = aircraft + "," + routeStops + "," + bestRoute + "," + feasibleRoute + "," + routeCost
    return data    

  
def notfeasibleToCsv(aircraft, routeStops, stops):
    feasibleRoute = "Not Feasible"
    routeCost = '0'            
    data = aircraft + "," + routeStops + "," + ","+ feasibleRoute + "," + routeCost      
    print("Route stops:", stops)
    print("This trip is not feasible in any combination.")
    print("-------------------------------------------------------------------------------------------------") 
    return data

def main(inputCsv, airportDict, currencyDict, aircraftDict):  
    '''The main function reads in each of the dictionaries for airports, currencies and aircrafts. It then uses these dictionaries
    and the methods within the classes, to extract distance and cost information, so cheapest route can be calculated'''
      
    # I only want to have the header in the bestroutes.csv once, so set a header   
    headerCount = 0 
    
    # open the testroutes.csv, I've taken a selection of options from Khalil's output.csv for the testroutes
    with open(os.path.join(inputCsv), "rt") as f:
        
        reader = csv.reader(f)
        
        # every line in the csv must be evaluated
        for line in reader:
            
            # error handling input file
            if (' ' in line):
                # if there is a whitespace in the CSV line
                print("There is a whitespace in this line of the file:")
                print(line)
                print("-------------------------------------------------------------------------------------------------") 
                continue
                # break out of this loop and move onto the next line
            stops = line
                   
            # have to assess if routes are feasible, initialise this flag as false
            feasible = False
            
            # the home and finish stop is the first element in the line input
            home = stops[0]
            
            # the aircraft is the 6th
            aircraft = stops[5]
            
            # get the range of the aircraft
            aircraftRange = aircraftDict.aircrafts[aircraft].getRange()
                   
            # route is the stops not including the home/finish
            # this is a like a queue as the order here does not matter, and I am only concerned with the first
            # element, and when I am done with it, I remove the head.
            # however to create each possible combination, I need to iterate over it which 
            # is not possible under the definition of a queue
            route = [stops[1], stops[2], stops[3], stops[4]]
        
            
            # comboKeys is a dictionary that will hold all possible combinations of routes, where the key 
            # is one of the 4 possible 2nd stop options, and the values are possible combinations, which all 
            # start with the key (possible 2nd stop)
            # home is appended to the front and end of each combination to complete the route
            # this is a set where the contents order does not matter
            comboKeys = airportDict.possibleCombinations(home, route)
            
            # Need a variable to keep track of the route with the cheapest cost   
            cheapestCost = 0
            
            # while the queue is not empty, use the head of the queue to carry out the below
            while len(route) != 0:
                # check if leg is valid, and get cost using the head and next element...
                value = comboKeys[route[0]]
                 # value returns the possible routes in the dictionary, given a key of an airport
                
                counter = 1
                
                for j in range(0,18,3):
                    option = value[j:j+3]
                    # option is an array of the each route option
                    counter += 1
        
                    option1 = list([option[0], option[1][0],  option[1][1],  option[1][2], option[1][3], option[2]])
                    # this is a list (sequence) as the order matters
        
                    cost = 0
                    stopCount = 0
                    for i in range(0,len(option1)-1):
                        # check distance validity and check associated cost
                        
                        distance = airportDict.getDistanceBetweenAirports(option1[i], option1[i+1])
                        countryName = airportDict.codes[option1[i]].getCountry()
        
                        if distance <= aircraftRange:
                            stopCount += 1
                            euroRate = currencyDict.currencies[countryName].getToEuroRate()
                            tripCost = airportDict.costOfTrip(euroRate, distance)
                            cost += tripCost

                            if stopCount == 5 and cost != 0:
                                totalCost = cost 
                                feasible = True
        
                        else:
                            break
                        
                    if feasible == True:
                        # if this is the first route option, cheapestCost will be 0, as it is intialised
                        if cheapestCost == 0:
                            cheapRoute = option1
                            cheapestCost = totalCost
                            
                        else:
                            if totalCost < cheapestCost:
                                cheapRoute = option1
                                cheapestCost = totalCost
                           
                # when finished with the top element of the queue, remove it
                route.remove(route[0])
            if headerCount == 0:     
                writeHeader() 
                headerCount += 1
                 
            aircraft = aircraft.replace('\''," ")
            routeStops = str(stops[0:5])
            # formatting the contents of routeStops to present nicely in the bestroutes.csv    
            for ch in ['[', ']', '\'', ',']:
                    if ch in routeStops:
                        routeStops = routeStops.replace(ch," ")    
               
            if feasible == True:
                data = feasibleToCsv(cheapRoute, cheapestCost, aircraft, routeStops, stops)      
                
            else:
                data = notfeasibleToCsv(aircraft, routeStops, stops)
                
            #return data #had a return value only for the purpose of the test file
            with open('bestroutes.csv','a') as file:
                file.write(data)
                file.write('\n')
                


if __name__ == "__main__":
    
    airportDict = AirportAtlas("./airport.csv")
    currencyDict = CurrencyAtlas("./currencyrates.csv", "./countrycurrency.csv")
    aircraftDict = AircraftAtlas("./aircraft.csv")
    main('./testroutes.csv', airportDict, currencyDict, aircraftDict)
    

