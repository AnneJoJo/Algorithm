def long_ones(arr):
    if arr == [] or len(arr) == 0:
        return 0
    idx = 0
    zero_bumper = 0
    max_len = 0
    while idx < len(arr) and zero_bumper < len(arr):
        if zero_bumper == len(arr) - 1 and arr[zero_bumper] == 1:
            tmp = zero_bumper - idx + 1
            max_len = max(max_len, tmp)
            break
        elif arr[idx] == 0 and arr[zero_bumper] == 0:
            idx += 1
            zero_bumper += 1

        elif arr[zero_bumper] == 0:

            tmp = zero_bumper - idx
            max_len = max(max_len,tmp)
            idx = zero_bumper + 1
            zero_bumper = idx

        else:
            zero_bumper += 1
    return max_len

print(long_ones([0,1,1,0,0,1,1,0]))