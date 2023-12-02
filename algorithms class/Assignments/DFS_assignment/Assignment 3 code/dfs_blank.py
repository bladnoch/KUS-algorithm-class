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
	time = 0  # global 시간
	card_V = G.get_card_V() #vertex 수
	color = [WHITE] * card_V  # vertex white으로 초기화
	pi = [None] * card_V
	d = [None] * card_V 	# discovery times
	f = [None] * card_V 	# finish times

	# Default order for starting searches goes from vertex 0 to vertex (card_V - 1).
	if order is None:
		order = range(card_V)
	# Visit each unvisited vertex.


	### ...TO BE COMPLETED ... ###
	for u in order: # 순서대로 vertex를 방문
		if color[u] == WHITE: # vertex 방문되지 않았다면(white), 그 vertex에서 DFS 시작
			dfs_visit(G, u) #dfs_visit() 호출

	return d, f, pi


def dfs_visit(G, u):
	"""Perform depth-first search on a graph represented by adjacency lists, starting
	from a given vertex.

	Arguments:
	G -- a graph, represented by adjacency lists.
	u -- root of the depth-first tree

	Updates the global timestamp time and the global lists color, pi, d, and f.
	"""
	global time, color, pi, d, f


	### ...TO BE COMPLETED ... ###

	color[u] = GRAY  # 정점 'u'를 방문 시작(gray)
	time += 1  # 시간 1 증가
	d[u] = time  # d 업데이트
	for v in G.get_adj_list(u):
		if color[v.get_v()] == WHITE:  # 아직 방문하지 않은(white) Vertex라면 실행
			pi[v.get_v()] = u
			dfs_visit(G, v.get_v())
	color[u] = BLACK  # 방문(검정)
	time += 1  # 시간 1 증가
	f[u] = time  # f 업데이트


# Testing
if __name__ == "__main__":

	vertices = ['u', 'v', 'x', 'y', 'w', 'z']
	edges = [('u', 'v'), ('u', 'x'), ('v', 'y'), ('w', 'y'),
			 ('w', 'z'), ('x', 'v'), ('y', 'x'), ('z', 'z')]
	graph1 = AdjacencyListGraph(len(vertices))
	for edge in edges:
		graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]))


	### ...TO BE COMPLETED ... ###

	# 모든 정점의 인접 리스트를 출력합니다.
	print("- Adjacency list for all vertices")
	for u in range(graph1.get_card_V()):
		print(f"{vertices[u]}: ", end="")
		for v in graph1.get_adj_list(u):
			print(f"{vertices[v.get_v()]} ", end="")
		print()


	# 깊이 우선 탐색을 수행하고 각 정점의 발견 시간(d), 완료 시간(f), 선행 정점(pi)를 출력합니다.
	d, f, pi = dfs(graph1) # dfs 함수로 깊이 우선 탐색을 수행하고 결과를 d, f, pi에 저장
	print("- Print d, f, pi for all vertices")
	for i in range(len(vertices)):
		print(f"{vertices[i]}: d = {d[i]}, f = {f[i]}, pi = {None if pi[i] is None else vertices[pi[i]]}")
