def subarray_product(arr):
    if len(arr) == 0 or arr == []:
        return 0
    max_dp = [1]*len(arr)
    min_dp = [1]*len(arr)
    max_dp[0] = arr[0]
    min_dp[0] = arr[0]
    res = arr[0]
    for i in range(1,len(arr)):

        min_dp[i] = min(arr[i],arr[i]*min_dp[i-1],arr[i]*max_dp[i-1])
        max_dp[i] = max(arr[i], arr[i]*min_dp[i-1], arr[i]*max_dp[i-1])

        res = max(res,max_dp[i])

    return  res

print(subarray_product([1,3,-4,-2]))

# space(1)

def sub_product(arr):
    if len(arr) == 0 or arr == []:
        return 0
    max_pre = 1
    min_pre = 1
    res = arr[0]
    for i in range(len(arr)):

        max_value = max(arr[i],arr[i]*max_pre,arr[i]*min_pre)
        min_value = min(arr[i],arr[i]*max_pre,arr[i]*min_pre)

        max_pre = max_value
        min_pre = min_value
        res = max(res,max_value)

    return res

print(subarray_product([-1,-8,2,3]))