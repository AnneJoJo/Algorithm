# difficult in code implementation
import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        
        4 0 5 0 -2  [0-5]
        4 9 5 4 -1  [4-9]
        10 9 5 5 -3 [5, 10]
        10 9 18 9 -2 [9, 18]
        10 12 18 -1 [10, 18]
        15 12 18 -2 [12, 18]
        15 20 18 -1 [15, 20]
        24 20 18 -3 [18, 24] 6
        24 20 22 -2 [20, 24] 4 
        
        """
        
        heap = []
        mimBase = float('inf')
        width = min([ len(n) for n in nums ]) 
        row = len(nums) # how many pointers
        #initialize the heap first
        for i in range(row):
            heapq.heappush(heap,[nums[i][0], i])
        pointer = [0]*row
        # any pointer in the array hits the width, break the loop,otherwise loop
        while True:
            [minVal,idx1] = heapq.heappop()
            [maxVal, idx2] = heapq.nlargest(1, heap)[0] 
            if (maxVal- minVal) < mimBase:
                res = [minVal, maxVal]
                mimBase = maxVal- minVal
            pointer[idx1] += 1
            if pointer[idx1] == width:
                break
            heapq.heappop(heap,[nums[idx1][pointer[idx1]], idx1])
            
            
        return res
            
        
            
            
        
        
            
            
            
                
                
                
            
        