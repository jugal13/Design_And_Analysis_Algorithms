graph={
	1 : [ 2, 3 ],
	2 : [ 1, 3, 4, 5 ],
	3 : [ 1, 2, 6, 7 ],
	4 : [ 2, 5, 8, 9],
	5 : [ 2, 4, 9],
	6 : [ 3, 7 ],
	7 : [ 3, 6 ],
	8 : [ 4, 9 ],
	9 : [ 4, 5, 8, 10 ],
	10 : [9]
}
layer = []
color = [""] * 20
def bfs(node):
	tree = []
	i = 0
	visited = [0]*11
	visited[node] = 1
	layer.append([node])
	print ("BFS Traversal\n")
	print (node)
	while layer[i]:
		r = []
		for u in layer[i]:
			for v in graph[u]:
				if visited[v] == 0:
					print (v)
					tree.append([u,v])
					visited[v] = 1
					r.append(v)
		layer.append(r)
		i += 1
	print ("\nBFS Tree")
	print (tree)
	print ("\nBFS Layers")
	return layer[:i]
print (bfs(1))