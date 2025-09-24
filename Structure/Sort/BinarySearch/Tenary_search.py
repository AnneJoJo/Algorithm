def tenary_search(arr,target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        left_mid = left + (right-left) // 3
        right_mid = right - (right-left) // 3

        if target == arr[left_mid]:
            return left_mid

        elif target == arr[right_mid]:
            return right_mid

        elif target < arr[left_mid]:
            right = left_mid - 1

        elif target > arr[right_mid]:
            left = right_mid + 1

        else:
            left = left_mid + 1
            right = right_mid - 1

    return - 1

print(tenary_search([1,2,4,5,6,7,8],2))

