#!/usr/bin/env python
import math
import sys
from datetime import datetime
from IOTSPData import readInput, writeOutput
from simulatedAnnealing import simulatedAnnealing

if (len(sys.argv) != 2):
    print "Usage: ./saDriver.py <PATH_TO_INPUT_FILE>"
    print "Example: ./saDriver.py ./TSP_Files-1/tsp_example_1.txt"
else:
    # Test InputFunction
    pathToInputFile = sys.argv[1]
    cities = readInput(pathToInputFile)
    # Print results
    print "------------------------------------------"
    startTime = datetime.now()
    distance, orderedListOfCities = simulatedAnnealing(cities)
    endTime = datetime.now()

    print "Total Running Time: ", str(endTime - startTime)
    print "Distance: ", distance
    print "------------------------------------------\n"

    writeOutput(pathToInputFile, distance, orderedListOfCities)
    
    
    print "\n NOTE: Running the Simulated Annealing Algorithm from tspDriver.py will give you time data and a formatted output"
