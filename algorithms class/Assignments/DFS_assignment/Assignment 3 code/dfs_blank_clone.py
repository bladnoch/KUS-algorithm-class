from adjacency_list_graph import AdjacencyListGraph
WHITE = 0  # undiscovered
GRAY = 1   # discovered
BLACK = 2  # visited

def dfs(G, order=None):
	"""Perform depth-first search on a graph represented by adjacency lists.

	Arguments:
	G -- a graph, represented by adjacency lists.
	order -- order of vertices in starting searches.  Defaults to the numerical order
	of the vertices.

	Returns:
	d -- list of vertex discovery times
	f -- list of vertex finish times
	pi -- list of depth-first vertex predecessors
	"""
	# Initialize color, pi, distance, and finish time lists.
	global time, color, pi, d, f
	time = 0  # global timestamp
	card_V = G.get_card_V()
	color = [WHITE] * card_V  # vertices are numbered, color[0] corresponds with color of vertex 0.
	pi = [None] * card_V
	d = [None] * card_V 	# discovery times
	f = [None] * card_V 	# finish times

	# Default order for starting searches goes from vertex 0 to vertex (card_V - 1).
	if order is None:
		order = range(card_V)
	# Visit each unvisited vertex.


	### ...TO BE COMPLETED ... ########################################################
	for u in order:
		if color[u] == WHITE:
			dfs_visit(G, u)

	return d, f, pi

	### ......END POINT....... ########################################################

def dfs_visit(G, u):
	"""Perform depth-first search on a graph represented by adjacency lists, starting
	from a given vertex.

	Arguments:
	G -- a graph, represented by adjacency lists.
	u -- root of the depth-first tree

	Updates the global timestamp time and the global lists color, pi, d, and f.
	"""
	global time, color, pi, d, f


	### ...TO BE COMPLETED ... ########################################################
	color[u] = GRAY
	time += 1
	d[u] = time
	for v in G.get_adj_list(u):
		if color[v.get_v()] == WHITE:
			pi[v.get_v()] = u
			dfs_visit(G, v.get_v())
	color[u] = BLACK
	time += 1
	f[u] = time
	### ......END POINT....... ########################################################

# Testing
if __name__ == "__main__":

	vertices = ['u', 'v', 'x', 'y', 'w', 'z']
	edges = [('u', 'v'), ('u', 'x'), ('v', 'y'), ('w', 'y'),
			 ('w', 'z'), ('x', 'v'), ('y', 'x'), ('z', 'z')]
	graph1 = AdjacencyListGraph(len(vertices))
	for edge in edges:
		graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]))


	### ...TO BE COMPLETED ... ########################################################

	d, f, pi = dfs(graph1)
	print(f"Discovery times: {d}")
	print(f"Finish times: {f}")
	print(f"Predecessors: {pi}")

	### ......END POINT....... ########################################################