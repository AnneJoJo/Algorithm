
def canJump(nums):
    '''
    Slow bottom up
    '''
    
    dp = [False]*len(nums)
    dp[-1] = True
    for i in range(len(nums)-2,-1,-1):
        steps = min(len(nums)-1, i+nums[i])
        for k in range(i,steps+1):
            if dp[k]:
                dp[i] = True
                break
           
    return dp[0]
       
        