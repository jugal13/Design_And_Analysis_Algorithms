items = {
	1 : [ 3, 10 ], 
	2 : [ 5, 4 ], 
	3 : [ 6, 9 ], 
	4 : [ 2, 11]
}
W = 7
M = [[0]*(W+1)]
for i in M:
	print(i)
def matrix():
	for i in range(1,len(items)+1):
		row = [0] 
		wi = items[i][0]
		vi = items[i][1]
		for w in range(1,W+1):
			if w < wi:
				row.append(M[i-1][w])
			else:
				row.append(max(M[i-1][w],vi+M[i-1][w-wi]))
		M.append(row)
	print ("\n\n")
	print (M)
	return M[len(items)][W]
def knapsack():
	result = []
	i = len(items)
	k = W
	while i > 0 and k > 0:
		wi = items[i][0]
		if M[i][k]!=M[i-1][k]:
			result.append(i)
			k = k-wi
		i = i-1
	return result
print (matrix())
print (knapsack())