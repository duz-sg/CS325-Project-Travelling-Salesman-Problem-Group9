#!/usr/bin/env python
import math
import sys
from sets import Set
from IOTSPData import readInput, writeOutput
from nearestNeighbor import nearestNeighborAlgorithm, repetitiveNearestNeighbor
from simulatedAnnealing import simulatedAnnealing

if (len(sys.argv) != 2):
    print "Usage: ./tspDriver.py <PATH_TO_INPUT_FILE>"
    print "Example: ./tspDriver.py ./TSP_Files-1/tsp_example_1.txt"
else:
    # Test InputFunction
    pathToInputFile = sys.argv[1]
    cities = readInput(pathToInputFile)

    # for city in cities:
    #     print city.i, " ", city.x, " ", city.y, " ", city.visited

    # Test output function
    # fakeDistance = 25
    # fakeListOfCities = [31, 23, 45]
    # writeOutput(pathToInputFile, fakeDistance, fakeListOfCities)

    # Calculate solution using algorithm of choice

    # Nearest Neighbor
    #distance, orderedListOfCities = nearestNeighborAlgorithm(cities, 0)
    # distance, orderedListOfCities = repetitiveNearestNeighbor(cities)
    distance, orderedListOfCities = simulatedAnnealing(cities)
    print('distance: ', distance)
    writeOutput(pathToInputFile, distance, orderedListOfCities)
