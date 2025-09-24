class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # check dup
                continue
            low = i + 1
            high = len(nums)-1

            while low < high:
                s = nums[low] + nums[i] + nums[high]
                if s == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:  # check dup
                        low += 1
                    while low < high and nums[high] == nums[high-1]:  # check dup
                        high -= 1
                    low += 1
                    high -= 1
                if s > 0:
                    high -= 1
                if s < 0:
                    low += 1
        return res
