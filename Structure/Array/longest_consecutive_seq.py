class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        numsSet = set(nums)
        
        longest = 0
        currentLen = 1
        for num in numsSet:
            if num - 1 not in numsSet:
                currentNum = num
                currentLen = 1
                while currentNum + 1 in numsSet:
                    currentNum += 1
                    currentLen += 1
                    
            longest = max(longest, currentLen)
            
        return longest

        #################Approach two######################
        def longestConsecutive(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if nums == []:
                return 0
            dp = [1] * len(nums)
            sortNums = sorted(nums)
            
            for i in range(1,len( sortNums)):
                if ( sortNums[i] - sortNums[i-1]) == 1:
                    dp[i] = dp[i-1] + 1
                elif sortNums[i] == sortNums[i-1]:
                    dp[i] = dp[i-1]
                
            return max(dp)
                

def conse_seq(arr):
    nums = set(arr)
    res = 0
    for each in nums:
         if each - 1 not in nums:
             cur_next = each
             while cur_next in nums:
                 cur_next += 1
             res = max(res, cur_next-each)
    return res