#!/usr/bin/env python
import math
import sys
from datetime import datetime
from IOTSPData import readInput, writeOutput
from simulatedAnnealing import simulatedAnnealing
from simulatedAnnealingParallel import simulatedAnnealingParallel

def printUsage():
    print "Usage: ./saDriver.py <PATH_TO_INPUT_FILE> ([p|s])"
    print "Example: ./saDriver.py ./TSP_Files-1/tsp_example_1.txt s     # Single Process"
    print "Example: ./saDriver.py ./TSP_Files-1/tsp_example_1.txt p     # Parallel Run"
    return

if (len(sys.argv) != 3):
    printUsage()
elif sys.argv[2] == 's':
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
elif sys.argv[2] == 'p':
    # Print results
    print "------------------------------------------"
    startTime = datetime.now()
    distance, orderedListOfCities = simulatedAnnealingParallel(cities)
    endTime = datetime.now()

    print "Total Running Time: ", str(endTime - startTime)
    print "Distance: ", distance
    print "------------------------------------------\n"

    writeOutput(pathToInputFile, distance, orderedListOfCities)
else:
    printUsage()
