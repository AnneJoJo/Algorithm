def zero_subarray(arr):
    if arr == [] or len(arr) == 0:
        return True

    # [1,1,5,8,3,-16]
    #0 1 2 7 15 18 2
    pos_sum = {}
    pos_sum[-1] = 0
    acc = 0
    for i,v in enumerate(arr):
        acc += v
        if acc in pos_sum.values():
            return True
        else:
            pos_sum[i] = acc

    return False

print(zero_subarray([1,2,-3,8,7]))

# print all combination
# we need to remeber the index and user[pre-valueIn hashMap:current_indx+1]