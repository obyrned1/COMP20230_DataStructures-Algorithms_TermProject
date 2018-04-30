'''
Created on 28 Mar 2018

@author: obyrned1
'''
import os.path
import csv
from math import pi,sin,cos,acos

with open(os.path.join("/home/obyrned1/Desktop/semester2/Data_Structures_&_Algorithms/assignment/input", 'airport.csv'), "rt") as f:
            reader = csv.reader(f)
            for line in reader:
                print(line)
                break