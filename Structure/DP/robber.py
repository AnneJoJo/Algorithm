'''
Either use array to differenciate status, or handle edge case first then use one array to
solve the problem:
            rob[i] = unrob[i-1] + nums[i-1]
            unrob[i] = max(unrob[i-1],rob[i-1])

dp equation is 

dp[i] = max(dp[i-2] + nums[i],dp[i-1])  

If we want to steal ,we can only add from dp[i-2]  
bottom up      
             
'''