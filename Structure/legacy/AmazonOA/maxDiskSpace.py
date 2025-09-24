import collections
class MaxOfMinima_MaximumDiskSpaceAvailable(object):
    def solution(self, nums, k): 
        dq=collections.deque()
        n=len(nums)
        res=0
        for i in range(n):
            if dq and dq[0]==i-k:
                dq.popleft()
        while dq and nums[dq[-1]]>nums[i]:
            dq.pop() 
        dq.append(i)
        if i>=k-1:
            res = max(res,nums[dq[0]] ) 
            
        return res
m = MaxOfMinima_MaximumDiskSpaceAvailable()
print(m.solution([1, 6, 7, 4, 8, 11, 9],3))