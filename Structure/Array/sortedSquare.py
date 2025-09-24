def sortedSquare(nums):
	newArr = [None] * len(nums)
	i = 0
	j = len(nums) - 1
	k = len(newArr) - 1

	while i <= j:
		a = nums[i]*nums[i]
		b = nums[j]*nums[j]

		if a >=b:
			newArr[k] = a 
			i += 1

		else:
			newArr[k] = b
			j -= 1

		k -= 1

	return newArr


print(sortedSquare([-3,-2,-1,0,8,9,10]))

def kthLargestElement(arr, k):
	if len(arr) < k: return -1
	return sorted(arr, reverse=True)[k-1]

import heapq
def kthLargestElement(arr, k):
	heap = []
	for n in arr:
		heapq.heappush(heap,-n)

	while k > 0 and len(heap) > 0:
		res = heapq.heappop(heap)

	return -res


def kthLargestElement(arr, k):

	def partition(nums, left, right):
		pivot = nums[left]
        l = left + 1
        r = right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        nums[left],nums[r] = nums[r],nums[left]
        
        return  r
        
	if k < len(arr): return -1
    left = 0
    right = len(nums) - 1
    while True:
            
        pos = partition(nums,left,right)
            
        if pos + 1 == k:
            return nums[pos] 
        if pos + 1 > k:
           right = pos - 1
        else:
            left = pos + 1
	


	






