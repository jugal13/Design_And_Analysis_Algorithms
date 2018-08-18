graph={
	1 : [ 2, 3 ],      
	2 : [ 1, 3, 4, 5 ],
	3 : [ 1, 2, 6, 7 ],
	4 : [ 2, 5, 8, 9 ],
	5 : [ 2, 4, 9 ],
	6 : [ 3, 7 ],
	7 : [ 3, 6 ],
	8 : [ 4, 9 ],
	9 : [ 4, 5, 8, 10 ],
	10 : [ 9 ]
}
def bfs(s):
	queue = []
	visited = [0]*len(graph)
	traversal = []
	visited[s-1] = 1
	queue.append(s)
	while queue:
		traversal.append(queue[0])
		u=queue.pop(0)
		for v in graph[u]:
			if visited[v-1] == 0:
				visited[v-1] = 1
				queue.append(v) 
	return traversal
traversal=bfs(1)
for i in traversal:
	print(i)

#Time Complexity O(|E|+|V|)