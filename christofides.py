import math
import sys

def create_graph(input_file):
	with open(input_file, 'r') as file:
		print "Opening file"
		cities = []
		x_coords = []
		y_coords = []
		edges = []

		i = 0
		for line in file:
			parsed = line.rsplit()
			cities.append(int(parsed[0]))
			x_coords.append(int(parsed[1])) 
			y_coords.append(int(parsed[2]))
			i += 1

		graph = [[0 for x in range(i)] for y in range (i)]

		for n in range(i):
			for m in range(i - n):
				x1 = x_coords[n]
				x2 = x_coords[m]
				y1 = y_coords[n]
				y2 = y_coords[m]
				graph[n][m] = math.sqrt(((x1 - x2)**2 + (y1 - y2)**2))
				edges.append((n, m))



	return graph, cities, edges

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



def blossom(vertices, edges):
	# Source: https://github.com/koniiiik/edmonds-blossom
	pass

def find_matching(graph, MST, odd):
	induced_graph = []

	for i in odd:
		for j in odd:
			if (i, j) not in induced_graph and (j, i) not in induced_graph:
				if graph[i][j] != 0: # Only take edges that are in the graph
					induced_graph.append((i, j))


	matching = []

	# for edge in induced_graph:
	# 	for v, u in edge:
	# 		if 

	return induced_graph


f = sys.argv[1]
g, v, e = create_graph(f)
t = create_mst(g)
o = find_odd_vertices(t, len(g))
i = find_matching(g, t, o)

for x in g:
	print x

for x in t:
	print x

for x in o:
	print x

for x in i:
	print x