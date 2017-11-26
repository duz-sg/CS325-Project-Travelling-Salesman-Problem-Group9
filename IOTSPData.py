#!/usr/bin/env python
import math
import sys

class city():
    i = ""
    x = ""
    y = ""
    visited = False

######################################
# Read from file ./inputFile.txt
######################################
def readInput(pathToInputFile):
    inputFile = open(pathToInputFile, "r")
    V = []
    with inputFile:
        for line in inputFile:
            parsedLine = map(int, line.rstrip().split())
            newCity = city()
            newCity.i = parsedLine[0]
            newCity.x = parsedLine[1]
            newCity.y = parsedLine[2]
            newCity.visited = False
            V.append(newCity)

    return V
    inputFile.close()

###################################
# Write to output File
###################################
def writeOutput(pathToInputFile, totalDistance, listOfCities):
    # for now I will stamp the end with tourTest so that it doesn't overwrite the examples
    print ("TODO - Change file extension from .tourTest to .tour before submitting project")
    outputFilePath = pathToInputFile + ".tourTest"
    outputFile = open(outputFilePath, 'w')

    # write the total distance
    outputFile.write(str(totalDistance))
    outputFile.write("\n")

    # write the list of cities
    for city in listOfCities:
        outputFile.write(str(city))
        outputFile.write("\n")
    outputFile.close()
