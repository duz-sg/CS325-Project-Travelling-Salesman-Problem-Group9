import math
import random
from random import shuffle

global numberOfCities

def linKernighan(listOfCities):
    # Reference: https://github.com/wilmerhenao/lin-kernighan/blob/master/lkmain.py

    global numberOfCities
    numberOfCities = len(listOfCities)
    newSolution = []
    improvement = 1

    bestSolution = list(listOfCities)  # Init the solution to be the path given by input txt
    bestDistance = E(bestSolution)

    while improvement > 0:
        currentSolution = bestSolution
        currentDistance = E(bestSolution)
        improvement = -1

        for i in range(0, numberOfCities):
            for j in range(2, numberOfCities-1):
                newSolution = bestSolution[0:j] + bestSolution[:j-1:-1]
                newDistance = E(newSolution)
                if newDistance < bestDistance:
                    improvement = bestDistance - newDistance
                    currentSolution = newSolution
                    currentDistance = newDistance
            if currentDistance < bestDistance:
                bestSolution = currentSolution
                bestDistance = E(bestSolution)
            bestSolution = [bestSolution[-1]] + bestSolution[0:-1]

    return E(bestSolution), bestSolution

def E(solution):
    # Calculate the total travel distance of the solution
    totalDistance = 0
    for i in range(0, numberOfCities):
        totalDistance += findDistance(solution[i-1], solution[i])
    return totalDistance

def P(currentDistance, newDistance, temperature):
    # Calculate the probability of accepting a new solution
    if newDistance < currentDistance:
        return 1
    else:
        return math.exp( -abs(newDistance - currentDistance) / temperature )

def findDistance(city1, city2):
    return int(round(math.sqrt( ((city1.x - city2.x)**2) + ((city1.y - city2.y)**2) )))

def getNeighbor(currentSolution):
    # Get a random neighbor by reversing a random sub-path of existing solution
    a = random.randint(2, numberOfCities-1)
    b = random.randint(0, numberOfCities-a)
    neighbor = list(currentSolution)
    neighbor[b:(b+a)] = reversed(neighbor[b:(b+a)])
    return neighbor
