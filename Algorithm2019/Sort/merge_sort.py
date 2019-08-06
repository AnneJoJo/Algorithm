def divided(arr):

    if len(arr) == 1:
        return arr

    l = 0
    r = len(arr)
    mid = (l + r) // 2


    left=divided(arr[:mid])

    right=divided(arr[mid:])

    ret = merge(left,right)

    return ret

def merge(left,right):
    res = []
    i,j = 0,0
    while i < len(left) or j < len(right):
       
        if i >= len(left):
            res.append(right[j])
            j += 1
        elif j >= len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return  res
# def merge(left,right):
#
#     res = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     if i != len(left):
#         res.extend(left[i:])
#     if j != len(right):
#         res.extend(right[j:])
#
#     return res

arr = [3,4,1,1,6,4,34,0]
print(divided(arr))


