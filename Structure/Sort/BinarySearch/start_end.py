def start_end(arr,target,flag):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high)//2

        if target < arr[mid] or (target == arr[mid] and flag):
            high = mid - 1

        else:
            low = mid + 1

    return low

arr = [4,5,5,5,6,7,8]
target = 5
start = start_end(arr,target,True)
end = start_end(arr,target,False)

print((start,end))

