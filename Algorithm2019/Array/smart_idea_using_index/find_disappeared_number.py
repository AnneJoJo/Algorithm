def find_disappeared_number(arr):
    """
    
    :param arr: start from 1 to n with dupilcate need to target missing numbers out
    :return: list
    """
    res = []
    for i in range(len(arr)):
        idx = abs(arr[i])-1
        if arr[idx] > 0:
            arr[idx] = - arr[idx]

    for j, vv in enumerate(arr,1):
        if vv > 0:
            res.append(j)

    return res


print(find_disappeared_number([4,3,2,7,8,2,3,1]))

