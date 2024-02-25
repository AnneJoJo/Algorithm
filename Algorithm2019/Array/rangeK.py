#   Input: nums = [1,3,6], k = 3
#   Output: 0
#   Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.

#  4 - 6 = -2
#  every elements should be count

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        return max(0, max(nums) - min(nums) - 2 * k)

