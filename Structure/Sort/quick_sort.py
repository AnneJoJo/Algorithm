# Two ways to implement quick sort
# 1. find pivot position and recursive by pivot position

def find_pivot(arr,low,high):
    """
    recursively by pivot position to sort arr using the idea of divided and conquer.
    :param arr: 
    :param low: 
    :param hight: 
    :return: 
    """
    if low < high:
        partition = compare_sort(arr,low,high)
        find_pivot(arr,low,partition)
        find_pivot(arr,partition+1,high)


def compare_sort(arr,low,high): # be carful about he boundray

    pivot = arr[low]
    left = low + 1
    right = high 

    while left <= right:
        if arr[left] > pivot and arr[right] < pivot:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -=1

        if arr[left] <= pivot:
            left += 1
        if arr[right] >= pivot:
            right -= 1
        
    arr[low],arr[right] = arr[right],arr[low]
   

    return right

def quick_sort(arr):

    find_pivot(arr,0,len(arr)-1)
    print(arr)


quick_sort([5,4,7,8,2])

