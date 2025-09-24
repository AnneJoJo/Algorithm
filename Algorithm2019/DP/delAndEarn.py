# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

# This is using number&Array trick
# when we can use number&Array trick:
# a sqequnce of positive integar 
'''
This issue is exact same to robber, we cannot earn the value adjacency.
We just need to conver it to the format we familar.
'''
import collections
def deleteAndEarn( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bucket = [0] * 10000
        count = collections.Counter(nums)
        
        for k,v in count.items():
            bucket[k] = k * v
        # build our bucket
        
        for i in range(2,len(bucket)):
           
                bucket[i] = max(bucket[i-1],bucket[i]+bucket[i-2]) 
            
        return bucket[-1]