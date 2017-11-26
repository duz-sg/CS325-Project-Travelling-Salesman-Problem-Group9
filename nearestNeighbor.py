import math

def findDistance(city1, city2):
    return int(round(math.sqrt( ((city1.x - city2.x)**2) + ((city1.y - city2.y)**2) )))


def findIndexOfClosestUnvisitedCity(currentCity, listOfCities):
    shortestDistance = float("inf")
    indexOfShortest = None

    # Loop through all the cities
    for i in range(0, len(listOfCities)):

        # Check if we have a new shortest distance to an unvisited city
        if (listOfCities[i].visited == False and
            findDistance(currentCity, listOfCities[i]) < shortestDistance):

            shortestDistance = findDistance(currentCity, listOfCities[i])
            indexOfShortest = i

    return indexOfShortest, shortestDistance

def nearestNeighborAlgorithm(V, startingIndex):
    # Initialize our currentCity as starting city
    currentCityIndex = startingIndex
    C = V[currentCityIndex]
    C.visited = True
    D = 0
    O = []
    O.append(C.i)

    # Find the order using nearest neighbor algorithm
    while (len(O) < len(V)):
        nextCityIndex, distanceToNext = findIndexOfClosestUnvisitedCity(C, V)

        # update current city to be the next city
        C = V[nextCityIndex]
        C.visited = True

        # add the distance to the next city to total
        D = D + distanceToNext

        # keep track of order
        O.append(C.i)

    # Add the distance to get back to the starting city
    distanceHome = findDistance(C, V[startingIndex])
    D = D + distanceHome
    return D, O

def repetitiveNearestNeighbor(V):
    # Initialize variables to held the best solutions that we can find
    D = float("inf")
    O = []

    # Try computing the nearest neighbor algorithm for each possible starting city
    for i in range(0, len(V)):

        # reset all cities to unvisited
        # TODO - use a toggle so that this loop is not necessary
        for j in range(0, len(V)):
            V[j].visited = False

        # determine path length and order
        d, o = nearestNeighborAlgorithm(V, i)

        # store result if it is the new best
        if (d < D):
            D = d
            O = o

    return D, O
