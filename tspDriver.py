#!/usr/bin/env python
import math
import sys
from datetime import datetime
from IOTSPData import readInput, writeOutput
from nearestNeighbor import nearestNeighborAlgorithm, repetitiveNearestNeighbor
from simulatedAnnealing import simulatedAnnealing

outputFileExtension = '.tour'

# Function for presenting results
def printResultsAndWriteOutput(distance, orderedListOfCities, startTime, endTime, title):
    # Print results
    print "------------------------------------------"
    print title
    print "Total Running Time: ", str(endTime - startTime)
    print "Distance: ", distance
    print "------------------------------------------\n"

    # Write results to output file for verification
    writeOutput(pathToInputFile, distance, orderedListOfCities, outputFileExtension)

def resetCitiesToUnvisited(cities):
    for city in cities:
        city.visited = 0

# Simple Nearest Neighbor Algorithm
def runNearestNeighbor(cities):
    print "Nearest Neighbor..."
    resetCitiesToUnvisited(cities)
    NOT_VISITED = 0
    VISITED = 1
    title = "Nearest Neighbor Algorithm Starting at Index 0"
    startTime = datetime.now()
    distance, orderedListOfCities = nearestNeighborAlgorithm(cities, 0, NOT_VISITED, VISITED)
    endTime = datetime.now()
    printResultsAndWriteOutput(distance, orderedListOfCities, startTime, endTime, title)

# Repetitive Nearest Neighbor Algorithm
def runRepetitiveNearestNeighbor(cities):
    print "Repetitive Nearest Neighbor..."
    resetCitiesToUnvisited(cities)
    title = "Repetitive Nearest Neighbor Algorithm (Try starting from all indexes and take best)"
    startTime = datetime.now()
    distance, orderedListOfCities = repetitiveNearestNeighbor(cities)
    endTime = datetime.now()
    printResultsAndWriteOutput(distance, orderedListOfCities, startTime, endTime, title)

# Simulated Annealing Algorithm
def runSimulatedAnnealingAlgorithm(cities):
    print "Simulated Annealing..."
    resetCitiesToUnvisited(cities)
    title = "Simulated Annealing Algorithm"
    startTime = datetime.now()
    distance, orderedListOfCities = simulatedAnnealing(cities)
    endTime = datetime.now()
    printResultsAndWriteOutput(distance, orderedListOfCities, startTime, endTime, title)


################################################
# Main Driver Program
################################################
if (len(sys.argv) != 2):
    print "Usage: ./tspDriver.py <PATH_TO_INPUT_FILE>"
    print "Example: ./tspDriver.py ./TSP_Files-1/tsp_example_1.txt"
else:
    # Setup
    pathToInputFile = sys.argv[1]
    cities = readInput(pathToInputFile)
    
    # Nearest Neighbor Algorithm (Single run using index 0 as starting city)
    # outputFileExtension = '.tour_Single-NN'
    # runNearestNeighbor(cities)

    # Repetitive Nearest Neighbor Algorithm
    outputFileExtension = '.tour_Repetitive-NN'
    runRepetitiveNearestNeighbor(cities)

    # Simulated Annealing
    #outputFileExtension = '.tour_SA'
    #runSimulatedAnnealingAlgorithm(cities)


    
    
