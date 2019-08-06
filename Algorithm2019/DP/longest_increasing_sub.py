#  [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

# not conitnuous
def long_incre_sub(arr):
    if len(arr) == 0 or arr == []:
        return 0

    res = 0
    dp = [1]*len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:

                dp[i] = max(dp[i],dp[j]+1)
        res = max(res,dp[i])

    return res

print(long_incre_sub([1,3,8,4,5,6]))


