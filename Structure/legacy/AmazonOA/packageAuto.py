def solution(arr): 
    arr.sort()
    for i in range(len(arr)):
        if i == 0: 
            arr[i] = 1
        else:
            if arr[i] > arr[i-1]+1:
                arr[i] = arr[i-1]+1 
    return arr[-1]


print(solution([3,2,3,5]))