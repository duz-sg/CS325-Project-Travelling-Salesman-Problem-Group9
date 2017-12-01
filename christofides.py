import math
import sys
from collections import defaultdict
# import blossom

def create_graph(input_file):
	with open(input_file, 'r') as file:
		print "Opening file"
		cities = []
		x_coords = []
		y_coords = []
		edges = []

		vert_dict = dict()

		i = 0
		for line in file:
			parsed = line.rsplit()
			cities.append(int(parsed[0]))
			x_coords.append(int(parsed[1])) 
			y_coords.append(int(parsed[2]))
			i += 1

		graph = [[0 for x in range(i)] for y in range (i)]

		for n in range(i):
			for m in range(i):
				x1 = x_coords[n]
				x2 = x_coords[m]
				y1 = y_coords[n]
				y2 = y_coords[m]
				graph[n][m] = int(math.sqrt(((x1 - x2)**2 + (y1 - y2)**2)))
				edges.append((n, m))
				vert_dict[(n, m)] = graph[n][m]

	return graph, vert_dict, edges, cities

def create_mst(graph):
	#Referemce -- https://gist.github.com/siddMahen/8261350

	MST = []			# The Minimum Spanning Tree to be returned
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

def find_odd_vertices(MST, n):

	odd = []
	for i in range(n):
		count = 0
		for edge in MST:
			if i in edge:
				count += 1

		if count % 2 != 0:
			odd.append(i)

	return odd


# Source: https://github.com/koniiiik/edmonds-blossom


def find_induced_graph(graph, MST, odd):
	induced_graph = []

	for i in odd:
		for j in odd:
			if (i, j) not in induced_graph and (j, i) not in induced_graph:
				if graph[i][j] != 0: # Only take edges that are in the graph
					induced_graph.append((i, j))

	return induced_graph

def create_multigraph(MST, mwpm, vertices):
	multigraph = MST + mwpm

	degrees = dict()

	for v in vertices:
		degree = 0
		for e in multigraph:
			if v in e:
				degree += 1

		degrees[v] = degree

	return multigraph, degrees


#Adapted from https://github.com/feynmanliang/Euler-Tour/blob/master/FindEulerTour.py
def find_euler_path(multigraph, vertices, degrees):

	graph = multigraph

	path = []

	start = graph[0][0]
	cur_vert = graph[0][0]

	# print "In Euler tour. Length of multigraph:"
	print len(graph)

	while len(graph) != 0:
		print "Top of loop. Length of graph: {}".format(len(graph))

		for e in graph:
			if cur_vert in e:



				print "Found edge {}".format(e)
				cur_edge = e
				path.append(cur_edge)
				if cur_vert == cur_edge[0]:
					cur_vert = cur_edge[1]
				elif cur_vert == cur_edge[1]:
					cur_vert = cur_edge[0]
				graph.remove(cur_edge)
				# print "Length of graph: {}".format(len(graph))

	return path

# Adapted from https://github.com/feynmanliang/Euler-Tour/blob/master/FindEulerTour.py
def find_euler_tour(graph):
	tour = []
	E = graph
	numEdges = defaultdict(int)

	def find_tour(u):
		for e in range(len(E)):
			if E[e] == 0:
				continue
			if u == E[e][0]:
				u, v = E[e]
				E[e] = 0
				find_tour(v)
			elif u == E[e][1]:
				v, u = E[e]
				E[e] = 0
				find_tour(v)
		tour.insert(0, u)

	for e in graph:
		i, j = e
		numEdges[i] += 1
		numEdges[j] += 1

	start = graph[0][0]
	current = start

	find_tour(current)

	return tour


def find_hamil_circuit(path):

	circuit = []

	for v in path:
		if v not in circuit:
			circuit.append(v)

	return circuit


def calculate_tour(graph, circuit):

	tour_weight = 0

	for i in range(len(circuit)):
		current = circuit[i]
		if i == len(circuit) - 1:
			i = -1
		else:
			i += 1
		next_node = circuit[i]
		tour_weight += graph[current][next_node]

	return tour_weight


f = sys.argv[1]
graph, vert_dict, edges, vertices = create_graph(f)
t = create_mst(graph)
o = find_odd_vertices(t, len(graph))
i = find_induced_graph(graph, t, o)

# for v in i:
# 	print v

with open("blossominput.txt", 'w') as bi:
	bi.write("{} {}\n".format(len(o), len(i)))
	for e in range(len(i)):
		v, u = i[e]
		w = graph[v][u]
		if w != 0:
			bi.write("{} {} {}\n".format(v, u, w))

mwpm = []

with open("blossomoutput.txt", "r") as bo:
	for line in bo:
		parsed = line.split()
		edge = (int(parsed[0]), int(parsed[1]))
		mwpm.append(edge)
		# print "+"


mg, degrees = create_multigraph(mwpm, t, vertices)

# for m in mg:
# 	print m

ep = find_euler_tour(mg)

# for e in ep:
# 	print e

c = find_hamil_circuit(ep)

# for v in c:
# 	print v

w = calculate_tour(graph, c)

print w