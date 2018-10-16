def upright(arr):
	#maxc = 1000000
	#maxr = 1000000

	if len(arr) > 100 or len(arr) < 1:
		return 

	m = 0
	for t in arr:
		if max(t) > m:
				m = max(t)
	if m > 1000000:
		return



	temp = [[0 for i in range(m)] for j in range(m)]


	for s in arr:
	#	print(s)
	#	print(s[1])
		for row in range(s[0]):
			for col in range(s[1]):
				temp[row][col] += 1

	#print(temp)
	print(temp[::-1])
	flatten = [y for x in temp[::-1] for y in x]
	num = max(flatten)
	return flatten.count(num)






if __name__== "__main__":
	arr = [(1,4),(2,3),(4,1)]
	print(upright(arr))