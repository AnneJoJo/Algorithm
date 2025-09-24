class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        1256
        
        tmp to save vivisted num in increasing order
        [5,2,6,1]
        [6,1]
        """
        tmp, res = [], []
        for i in range(len(nums)-1,-1,-1):
            left = 0
            right = len(tmp) 
            
            while left < right:
                mid = (left + right) // 2
                if nums[i] > tmp[mid]:
                    left = mid + 1
                    
                else:
                    right = mid 
                    
                    
            res.insert(0,right)
            tmp.insert(right, nums[i])
            
        return res
                    
       
            
            