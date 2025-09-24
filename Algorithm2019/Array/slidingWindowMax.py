# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


7 

# maintian a Deque with len k 
# q = []

# [1]
# loop the array  with i 
# i - q[0] + 1 == k: 
#     save the arr[q[-1]] to ret
#     pop first element 1 
#     [3] idx = 3-1+1 == k 
#     save the arr[q[-1]] to ret 
#     pop first element

# if next > q[-1]: (save index)
#     append next to q [0, 1 ] 
# else:
#     continue 




def maximum(arr, k):
    dequeue = []
    ret = []
    
    
    
    return ret
       
            
        
            