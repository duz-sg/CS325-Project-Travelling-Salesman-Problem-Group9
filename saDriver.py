#!/usr/bin/env python
import math
import sys
from datetime import datetime
from IOTSPData import readInput, writeOutput
from simulatedAnnealing import simulatedAnnealing
from simulatedAnnealingParallel import simulatedAnnealingParallel

def printUsage():
    print
    print "Usage: ./saDriver.py <PATH_TO_INPUT_FILE> <MODE>"
    print "Example: ./saDriver.py ./TSP_Files-1/tsp_example_1.txt fast     # Fast, better speed"
    print "Example: ./saDriver.py ./TSP_Files-1/tsp_example_1.txt normal   # Normal"
    print "Example: ./saDriver.py ./TSP_Files-1/tsp_example_1.txt slow     # Slow, shorter distance"
    print
    return

if (len(sys.argv) != 3):
    printUsage()
else:
    # Test InputFunction
    pathToInputFile = sys.argv[1]
    coolDownRate = 0.99995
    if sys.argv[2] == 'fast':
        coolDownRate = 0.9995
    elif sys.argv[2] == 'normal':
        coolDownRate = 0.99995
    elif sys.argv[2] == 'slow':
        coolDownRate = 0.999995
    else:
        printUsage()
        exit()

    cities = readInput(pathToInputFile)
    # Print results
    print "------------------------------------------"
    startTime = datetime.now()
    distance, orderedListOfCities = simulatedAnnealing(cities, coolDownRate)
    endTime = datetime.now()

    print "Total Running Time: ", str(endTime - startTime)
    print "Distance: ", distance
    print "------------------------------------------\n"

    extension = ".tour-SA-" + sys.argv[2]
    writeOutput(pathToInputFile, distance, orderedListOfCities, extension)
