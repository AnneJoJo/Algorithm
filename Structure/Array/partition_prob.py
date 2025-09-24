def partition_pro(arr):
    target = sum(arr) / 3
    if arr == [] or len(arr) <= 1 or sum(arr) % 2 == 1:
        return False
    dp = [False] * (target + 1)
    dp[0] = True
    for each in arr:
        if each <= target:
            for j in range(each, target + 1)[::-1]:
                dp[j] = dp[j] or dp[j - each]

    return dp[target]

print(partition_pro([7,3,5,12,2,1,5,3,8,4,6,4]))

# follow up k partition and print them all
# think about k == 3 first if two set exisit then rest will be the third one
# recurisve brute force