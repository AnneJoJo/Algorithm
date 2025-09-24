class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = -float('inf')
        cum = -float('inf')
        start = 0
        for i, v in enumerate(nums):
            if cum + v < v:
                start = i
                cum = v
            else:
                cum += v
            maxVal = max(maxVal, cum)

        return maxVal

