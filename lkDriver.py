#!/usr/bin/env python
import math
import sys
from datetime import datetime
from IOTSPData import readInput, writeOutput
from linKernighan import linKernighan

def printUsage():
    print
    print "Usage: ./lkDriver.py <PATH_TO_INPUT_FILE> "
    print "Example: ./lkDriver.py ./TSP_Files-1/tsp_example_1.txt"
    print
    return

if (len(sys.argv) != 2):
    printUsage()
else:
    # Test InputFunction
    pathToInputFile = sys.argv[1]

    cities = readInput(pathToInputFile)
    # Print results
    print "------------------------------------------"
    startTime = datetime.now()
    distance, orderedListOfCities = linKernighan(cities)
    endTime = datetime.now()

    print "Total Running Time: ", str(endTime - startTime)
    print "Distance: ", distance
    print "------------------------------------------\n"

    extension = ".tour-LK"
    writeOutput(pathToInputFile, distance, orderedListOfCities, extension)
