def replaceMaxValueFromRight(arr):
	
	'''
		[17,18,5,4,6,1]
				   1 -1
				6 6 1 -1
	'''
	rightMax = -1

	for i in range(len(arr)-1, -1, -1):

		val = rightMax

		rightMax = max(rightMax,arr[i]) # for the next round 1

		arr[i] = val

	return arr


print(replaceMaxValueFromRight([17,18,5,4,6,1]))