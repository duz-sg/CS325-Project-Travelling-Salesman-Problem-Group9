# Read the list of vertices in as an array, V
# Initialize a variable, D, to indicate the shortest distance found for our optimal solution
# Initialize an array, O, to indicate the best order for our optimal tour
# Initialize a variable, i = 0, to indicate which city will be our first starting city
# While i < length of V, i++
    # Initialize a variable, d = 0, to store the total distance of the tour being calculated in this iteration
    # Initialize an array to hold the order, o, in which the vertices are visited in this iteration
    # Mark all vertices in V as not visited
    # Initialize the current vertex, C = V[i], our starting city
    # Push C into the array of visited vertices, o
    # While (length of o) < (length of V):
        # Find the closest vertex in V that has not been visited, N
        # Add the distance from C to N onto d
        # Push the N into o to keep track of the order
        # Mark C as visited
        # Add the distance from C back to the starting vertex to d
        # Keep track of the best solution that we have found
        # If (d < D)
        # D = d
        # O = o