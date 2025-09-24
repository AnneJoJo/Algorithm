# You are given an array nums of n positive integers.

# You can perform two types of operations on any element of the array any number of times:

# If the element is even, divide it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
# If the element is odd, multiply it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.

# Return the minimum deviation the array can have after performing some number of operations.

#  If we have increased all numbers to their maximum,
#  then we can not increase minimum. If we want smaller deviation, we can only decrease maximum.

import heapq
class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        find minumum let maximum decrease and close to min
        """
        heap = []
        minValue = float('inf')
        for num in nums:
            if num %2 == 0:
                heap.append(-num)
                minValue = min(minValue, num)
            else:
                heap.append(-num*2)
                minValue = min(minValue, num*2)
       
        heapq.heapify(heap)
        minDeviateValue = float('inf')
        while heap:
            curValue = -heapq.heappop(heap) #negative min == positive largest
           
            minDeviateValue = min(minDeviateValue, curValue-minValue)
            if curValue % 2 == 0:
                minValue = min(minValue, curValue//2)
               
                heapq.heappush(heap, -curValue//2)
            else:
                
                break
        
        return minDeviateValue
                
        
                
        