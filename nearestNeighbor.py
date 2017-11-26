import math


def findDistance(city1, city2):
    return int(round(math.sqrt( ((city1.x - city2.x)**2) + ((city1.y - city2.y)**2) )))


def findIndexOfClosestUnvisitedCity(currentCity, listOfCities, NOT_VISITED, VISITED):
    shortestDistance = float("inf")
    indexOfShortest = None

    # Loop through all the cities
    for i in range(0, len(listOfCities)):

        # Check if we have a new shortest distance to an unvisited city
        if (listOfCities[i].visited == NOT_VISITED and
            findDistance(currentCity, listOfCities[i]) < shortestDistance):

            shortestDistance = findDistance(currentCity, listOfCities[i])
            indexOfShortest = i

    return indexOfShortest, shortestDistance

def nearestNeighborAlgorithm(V, startingIndex, NOT_VISITED, VISITED):

    # Initialize our currentCity as starting city
    currentCityIndex = startingIndex
    C = V[currentCityIndex]
    C.visited = VISITED
    D = 0
    O = []
    O.append(C.i)

    # Find the order using nearest neighbor algorithm
    while (len(O) < len(V)):
        nextCityIndex, distanceToNext = findIndexOfClosestUnvisitedCity(C, V, NOT_VISITED, VISITED)

        # update current city to be the next city
        C = V[nextCityIndex]
        C.visited = VISITED

        # add the distance to the next city to total
        D = D + distanceToNext

        # keep track of order
        O.append(C.i)

    # Add the distance to get back to the starting city
    distanceHome = findDistance(C, V[startingIndex])
    D = D + distanceHome
    return D, O

def repetitiveNearestNeighbor(V):

    # Initialize variables that will be toggled to avoid extra looping
    NOT_VISITED = 0
    VISITED = 1

    # Initialize variables to held the best solutions that we can find
    D = float("inf")
    O = []

    # Try computing the nearest neighbor algorithm for each possible starting city
    for i in range(0, len(V)):

        # determine path length and order
        d, o = nearestNeighborAlgorithm(V, i, NOT_VISITED, VISITED)

        # store result if it the new best
        if (d < D):
            D = d
            O = o
        
        # we are done with loop, toggle VISITED and NOT_VISITED
        if (NOT_VISITED == 0):
            NOT_VISITED = 1
            VISITED = 0
        else:
            NOT_VISITED = 0
            VISITED = 1

    return D, O
