def findMediumFromArray(arr):
	'''
		array is unsorted
		# approach 1 sort

        	# appraoch 2 selection

        	# approch 3 bucket sort
	'''

	bucket = [None]*(max(arr)+1)
	for n in arr:
		bucket[n] = 1
	
	def bucketSort(arr,bucket):
		left = 0
		
		count = (len(arr) // 2) + 1
		pre = 0
		
		while count > 0:
			if bucket[left] == 1:
				count -= 1
				if count == 1:
					pre = left 
			left += 1
		mid = left - 1

		if len(arr) % 2 == 0:
			return (mid + pre)/2
		else:
			return mid
	
	return bucketSort(arr, bucket)


print(findMediumFromArray([5,3,1,6]))