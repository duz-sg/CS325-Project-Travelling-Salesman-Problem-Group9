import math
import random
from random import shuffle
from nearestNeighbor import nearestNeighborAlgorithm
from multiprocessing import Pool

global numberOfCities

def simulatedAnnealingParallel(listOfCities):
    # Let s = s0
    # For k = 0 through kmax (exclusive):
    #   T <- temperature(k / kmax)
    #   Pick a random neighbour, snew <- neighbour(s)
    #   If P(E(s), E(snew), T) >= random(0, 1):
    #       s <- snew
    # Output: the final state s

    currentSolution = list(listOfCities)  # Init the solution to be the path given by input txt
    #distance, currentSolution = nearestNeighborAlgorithm(listOfCities, 0, 0, 1) # Init the solution using Nearest Neighbor Algorithm

    global numberOfCities
    numberOfCities = len(listOfCities)
    newSolution = []
    N = 24          # Numer of Processes
    T = 1000        # Temperature
    C = 0.99995     # Cooling rate
    k = 0
    pool = Pool(N)

    while T > 0.000000000000001:
        args = [currentSolution] * N
        results = pool.map(getNeighbor, args)

        distances = []
        minDistance = float("inf")
        for result in results:
            if result[0] < minDistance:
                minDistance = result[0]
                newSolution = result[1]

        if P(E(currentSolution), minDistance, T) >= random.random():
            print "Step: ", k, "Temperature: ", T, "Distance: ", minDistance
            currentSolution = list(newSolution)
        k += N
        T *= C**N

    pool.close()
    pool.join()
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
    return E(neighbor), neighbor
