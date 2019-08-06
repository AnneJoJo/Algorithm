def sell_stock(arr):
    # arr = [1,5,2,3,7,6,4,5]

    acc_min = 0

    for i in range(1,len(arr)):

        if arr[i] > arr[i-1]:
            acc_min += arr[i] - arr[i-1]


    return acc_min

print(sell_stock([1,5,2,3,7,6,4,5]))


