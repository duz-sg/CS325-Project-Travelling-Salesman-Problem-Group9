import math
import sys
from collections import defaultdict
import blossom

# Create graph from input file
def create_graph(input_file):
	with open(input_file, 'r') as file:
		cities = []		# Holds the vertex numbers -- line item 0
		x_coords = []	# Holds x coordinates -- line item 1
		y_coords = []	# Holds y coordinates -- line item 2
		edges = []		# A list of tuples representing edges between vertices

		weight_dict = dict()	# A dictionary mapping edges to weight values

		for line in file:
			parsed = line.rsplit()			# Split the line up
			cities.append(int(parsed[0]))
			x_coords.append(int(parsed[1])) 
			y_coords.append(int(parsed[2]))

		# Number of Vertices
		size = len(cities)

		# graph - Holds a distance matrix representing the graph in total
		graph = [[0 for x in range(size)] for y in range (size)]

		# Fill the graph
		for n in range(size):
			for m in range(size):
				x1 = x_coords[n]
				x2 = x_coords[m]
				y1 = y_coords[n]
				y2 = y_coords[m]					# vv Calculate weight vv
				graph[n][m] = int(round(math.sqrt(((x1 - x2)**2 + (y1 - y2)**2))))
				edges.append((n, m))				# Add to edges
				weight_dict[(n, m)] = graph[n][m]	# Fill the dictionary of weights

	return graph, weight_dict, edges, cities		# Return everything we'd ever need

# Create a Minimum Spanning Tree from the passed in graph (as a distance matrix)
# Source -- https://gist.github.com/siddMahen/8261350
def create_mst(graph):

	MST = []			# The Minimum Spanning Tree to be returned -- A list of edges (tuples)
	visited = set() 	# The set of edges already connected

	# select an arbitrary vertex to begin with
	visited.add(0);

	while len(visited) != len(graph):	# Loop until we've included every node
		
		crossing = set()
		# for each element x in visited, add the edge (x, k) to crossing if
		# k is not in visited
		for x in visited:
			for k in range(len(graph)):
				if k not in visited and graph[x][k] != 0:
					crossing.add((x, k))
		# find the edge with the smallest weight in crossing
		edge = sorted(crossing, key=lambda e:graph[e[0]][e[1]])[0];
		# add this edge to MST
		MST.append(edge)
		# add the new vertex to visited
		visited.add(edge[1])

	return MST

# Returns a list of odd vertices in the MST for use in building an induced graph
def find_odd_vertices(MST, n):

	odd = []
	for i in range(n):
		count = 0
		for edge in MST:
			if i in edge:
				count += 1	# Determine degree of each vertex

		if count % 2 != 0:	# Add odd vertices to the list
			odd.append(i)

	return odd

# Creates an induced graph by connecting the vertices of odd degree
def find_induced_graph(graph, odd):
	induced_graph = []

	for i in odd:
		for j in odd:
			if (i, j) not in induced_graph and (j, i) not in induced_graph: # We don't need duplicate edges here
				if graph[i][j] != 0: # Only take edges that are in the graph
					induced_graph.append((i, j))

	return induced_graph


def create_multigraph(MST, mwpm):
	multigraph = MST + mwpm
	return multigraph

# Returns a Eulerian tour (actually a circuit) given the inputed multigraph
# Source -- https://github.com/feynmanliang/Euler-Tour/blob/master/FindEulerTour.py
def find_euler_tour(multigraph):
	
	graph = multigraph

	tour = []
	numEdges = defaultdict(int)
	
	# Recursively finds a Eulerian tour from a given starting node
	def find_tour(u):
		
		for e in range(len(graph)):
			if graph[e] == 0:		# Skip empty edges
				continue
			if u == graph[e][0]:	# If the vertex u is the first vertex of the first edge
				u, v = graph[e]
				graph[e] = 0
				find_tour(v)
			elif u == graph[e][1]:	# If the vertex u is the second vertex of the first edge
				v, u = graph[e]
				graph[e] = 0
				find_tour(v)
		
		# Insert each vortex as the recursive calls return
		tour.insert(0, u)

	# Count the number of edges incident on each vertex
	for e in graph:
		i, j = e
		numEdges[i] += 1
		numEdges[j] += 1

	start = graph[0][0]

	current = start
	find_tour(current)

	return tour


# Finds a Hamiltonian circuit using the Eulerian circuit -- This is our TSP Tour!
def find_ham_circuit(path):

	circuit = []

	for v in path:				# Shortcut at node that is already in the list
		if v not in circuit:
			circuit.append(v)

	return circuit 				# Returns the Ham-Circuit, which is the final TSP tour


# Takes the graph and the final tour, and calculates the actual weight
def calculate_tour(graph, circuit):

	tour_weight = 0

	for i in range(len(circuit)):
		current = circuit[i]
		if i == len(circuit) - 1:	# Break on the last node and handle completing the circuit separately
			break
		else:
			i += 1								 # Look ahead to the next node
		next_node = circuit[i]		
		tour_weight += graph[current][next_node] # Add the weight of the edge to the total

	tour_weight += graph[circuit[0]][circuit[-1]]		# Account for the final 

	return tour_weight


def run_christofides(input_file):
	file = input_file

	# Variables:
	# * graph is a distance matrix representing the entire graph
	# * weight_dict is a dictionary with edges as keys and weights as values
	# * edges is a list of edges represented as tuples
	# * vertices is a list of the numerical labels of each vertex
	graph, weight_dict, edges, vertices = create_graph(file)	# Unpack return values of create_graph()

	# * tree is the MST created from graph, represented by a list of edges
	tree = create_mst(graph)

	# * odd is simply the list of odd-degree vertices in tree
	odd = find_odd_vertices(tree, len(graph))

	# * induced is a graph formed by connecting the edges in odd
	induced = find_induced_graph(graph, odd)

	# These will hold inputs for the blossom algorithm call below
	induced_edges = []
	induced_weights = []

	# Fill the above lists with their respective data
	for e in range(len(induced)):
		v, u = induced[e]	# Unpack the edges
		w = graph[v][u]		
		induced_edges.append((v, u)) # Fill the edge list
		induced_weights.append(w)	 # Fill the weights list

	# Source of blossom code: https://github.com/koniiiik/edmonds-blossom
	# Edmonds' Blossom algorithm allows us to find a minimum weight perfect matching of the induced graph
	# Code contained in blossom.py, modified slightly to accomodate different input and output formats
	# * matching is the list of edges in the Minimum Weight Perfect Matching of the induced graph
	matching = blossom.calculate_matching(induced_edges, induced_weights)

	# * multi_graph is a graph formed by merging the edges in tree with the edges in tree 
	multi_graph = create_multigraph(matching, tree)

	# * euler_path is the Eulerian Circuit created by traversing every edge of the multigraph once -- a list of vertices
	euler_path = find_euler_tour(multi_graph)

	# * ham_circuit is the Hamiltonian circuit obtained by shortcutting any repeated nodes in euler_path -- also a list of vertices
	ham_circuit = find_ham_circuit(euler_path)	# ham_circuit is our final TSP tour!

	# * total_weight is the final tour cost calculated by traversing ham_circuit
	total_weight = calculate_tour(graph, ham_circuit)

	# Handle output within Project paramters
	filename = input_file + ".tour_Christofides"

	with open(filename, 'w') as output:
		output.write(str(w) + "\n")
		for v in ham_circuit:
			output.write(str(v) + "\n")
		output.write(str(0))

	# Return our results in case anyone is listening
	return total_weight, ham_circuit