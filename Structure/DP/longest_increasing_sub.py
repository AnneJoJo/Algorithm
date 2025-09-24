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


# nlogn

def long_increse_sub(arr):
    if len(arr) == 0 or arr == []:
        return 0

    order_arr = [0]

    for i in range(1,len(arr)):
        if arr[order_arr[-1]] < arr[i]:
            order_arr.append(i)
        else:
            binary_replace(order_arr,arr,i)
    #print_res(arr,order_arr)
    return  len(order_arr)

def binary_replace(order, arr, idx):
    low = 0
    high = len(order) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[order[mid]] < arr[idx]:
            low = mid + 1
        else:
            high = mid - 1

    order[low] = idx
def print_res(arr,order):
    while order:
        idx = order.pop(0)
        print(arr[idx])

print(long_increse_sub([3,4,-1,5,8,2,3,12,7,9,10]))
print(long_increse_sub([1,3,8,4,5,6]))




