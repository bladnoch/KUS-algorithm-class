from adjacency_list_graph import AdjacencyListGraph
WHITE = 0  # undiscovered
GRAY = 1   # discovered
BLACK = 2  # visited

def dfs(G, order=None):
	global time, color, pi, d, f
	time = 0
	card_V = G.get_card_V()
	color = [WHITE] * card_V
	pi = [None] * card_V
	d = [None] * card_V
	f = [None] * card_V

	if order is None:
		order = range(card_V)

	for u in order:
		if color[u] == WHITE:
			dfs_visit(G, u)




def dfs_visit(G, u):
	global time, color, pi, d, f
	time = time + 1
	d[u] = time
	color[u] = GRAY

	for edge in G.get_adj_list(u):  # G.get_adj_list(u)는 정점 u의 모든 인접 정점들을 반환합니다.
		v = edge.get_v()
		if color[v] == WHITE:
			pi[v] = u
			dfs_visit(G, v)

	color[u] = BLACK
	time = time + 1
	f[u] = time



if __name__ == "__main__":
	vertices = ['u', 'v', 'x', 'y', 'w', 'z']
	edges = [('u', 'v'), ('u', 'x'), ('v', 'y'), ('w', 'y'),
			 ('w', 'z'), ('x', 'v'), ('y', 'x'), ('z', 'z')]
	graph1 = AdjacencyListGraph(len(vertices))
	for edge in edges:
		graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]))

	dfs(graph1)

	for v in range(graph1.get_card_V()):
		print(f"{vertices[v]}: d = {d[v]}, f = {f[v]}, pi = {None if pi[v] is None else vertices[pi[v]]}")
