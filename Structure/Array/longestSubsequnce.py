def lengthOfLIS(nums):
        """
        :type nums: List[int]
        :rtype: int
        [10,9,2,5,3,7,101,18]

        res [2,3,7,18]
        """
        if nums == None or len(nums) == 0:
            return 0

        res = []
        for n in nums:
            i = 0
            j = len(res)
            while i < j:
                mid = (i + j) // 2
                if res[mid] < n:
                    i = mid + 1
                else:
                    j = mid
            if j >= len(res):
                res.append(n)
            else:
                res[j] = n

        print(res)      
        return len(res)into

lengthOfLIS([10,9,2,5,3,7,101,18])


#method 2
def lengthOfLIS(nums):
    dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
                    
            res = max(res,dp[i])
        return res
                    
                