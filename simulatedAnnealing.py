import math
import random
from random import shuffle
from nearestNeighbor import nearestNeighborAlgorithm

global numberOfCities

def simulatedAnnealing(listOfCities, coolDownRate):
    # Let s = s0
    # For k = 0 through kmax (exclusive):
    #   T <- temperature(k / kmax)
    #   Pick a random neighbour, snew <- neighbour(s)
    #   If P(E(s), E(snew), T) >= random(0, 1):
    #       s <- snew
    # Output: the final state s

    global numberOfCities
    numberOfCities = len(listOfCities)
    newSolution = []

    currentDistance, currentSolution = nearestNeighborAlgorithm(listOfCities, 0, 0, 1) 
    #currentSolution = list(listOfCities)  # Init the solution to be the path given by input txt
    #currentDistance = E(currentSolution)

    T = round(math.sqrt(numberOfCities))    # Temperature
    C = coolDownRate or 0.99995             # Cooling rate
    S = 0.000000000000001                   # Stop temperature
    k = 0

    while T > S:
        newSolution = getNeighbor(currentSolution)
        newDistance = E(newSolution)
        if P(currentDistance, newDistance, T) >= random.random():
            currentSolution = list(newSolution)
            currentDistance = newDistance
        if k % 1000 == 0:
            print "Step: ", k, "Temperature: ", T, "Distance: ", currentDistance
        k += 1
        T *= C

    return E(currentSolution), currentSolution

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
