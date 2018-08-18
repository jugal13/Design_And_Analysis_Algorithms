import random
from time import clock
def sel_sort(a) :
	m = 0
	for i in range(n-1) :
		m = i
		for j in range(i+1, n) :
			if a[j] < a[m] :
				m = j
		a[i] , a[m] = a[m] , a[i]
	return a
def ins_sort(arr) :
	for i in range(1,len(arr)) :
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key :
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	return arr
def merge(a,b):
	m = []
	if a[0] <= b[0]:
		m.append(a.pop(0))
	else:
		m.append(b.pop(0))
	m += a
	m += b
	return m
def mer_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr)//2
	b = mer_sort(arr[:mid])
	c = mer_sort(arr[mid:])
	d = merge(b,c)
	return d

times = [100,200,300,500,1000,2000,3000,5000,6000,8000,10000,50000]
print ("n\tMerge\tInsertion\tSelection\n")
for i in times:
	x = random.sample(range(i),i)
	tm = clock()
	xm = mer_sort(x)
	tm = clock() - tm
	ti = clock()
	xi = ins_sort(x)
	ti = clock() - ti
	ts = clock()
	print (i,"\t",tm,"\t",ti,"\t",ts,"\n")