import math
import sys
# import blossom

def create_graph(input_file):
	with open(input_file, 'r') as file:
		print "Opening file"
		cities = []
		x_coords = []
		y_coords = []
		edges = []

		vertices = dict()

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
				vertices[(n, m)] = graph[n][m]

	return graph, vertices, edges

def create_mst(graph):
	#source -- https://gist.github.com/siddMahen/8261350

	MST = set() 		# The Minimum Spanning Tree to be returned
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
		MST.add(edge)
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

def find_mwmp(vertices):
	return blossom.calculate_mwmp(vertices)




def find_induced_graph(graph, MST, odd):
	induced_graph = []

	for i in odd:
		for j in odd:
			if (i, j) not in induced_graph and (j, i) not in induced_graph:
				if graph[i][j] != 0: # Only take edges that are in the graph
					induced_graph.append((i, j))

	# matching = []

	# for edge in induced_graph:
	# 	for v, u in edge:
	# 		if 

	return induced_graph


f = sys.argv[1]
graph, vertices, edges = create_graph(f)
t = create_mst(graph)
o = find_odd_vertices(t, len(graph))
i = find_induced_graph(graph, t, o)

with open("blossominput.txt", 'w') as bl:
	bl.write("{} {}\n".format(len(graph), len(vertices) - len(graph)))
	for v, w in vertices.items():
		if w != 0:
			bl.write("{} {} {}\n".format(v[0], v[1], w))

