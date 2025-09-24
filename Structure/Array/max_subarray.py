def max_sub(arr):

    cur_max = 0
    max_val = 0
    if max(arr) < 0:
        return max(arr)
    for i in range(len(arr)):
        cur_max += arr[i]
        if arr[i] > cur_max:
            cur_max = arr[i]
        
        max_val = max(max_val,cur_max)

    return  max_val


print(max_sub([-1,-3,-4,-5,-3]))