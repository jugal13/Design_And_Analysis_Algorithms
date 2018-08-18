import time
def binary_search(A,low,high):
	key = 100
	mid = (low+high)/2
	if A[mid] == key:
		return mid+1
	elif A[mid] > key:
		return binary_search(A,mid-1,high)
	elif A[mid] < key:
		return binary_search(A,low,mid+1)
	else:
		return -1

A = [x for x in range(90000000)]
start = time.clock()
print (binary_search(A,len(A)-1))
stop = time.clock()
print (stop-start)