def sub_eaq_sum(arr,target):
    # [5,6,-5,5,3,5,3,-2,0]
    pos_sum = {}
    pos_sum[0] = -1
    acc = 0
    res = []
    max_length = 0
    for i in range(len(arr)):
        acc += arr[i]
        if not acc in pos_sum:
            pos_sum[acc] = i
        if acc - target in pos_sum:
            start_idx = pos_sum[acc-target]
            if max_length < (i - start_idx):
                max_length = i - start_idx
                res = arr[start_idx+1:i+1]
    print(pos_sum)
    return res

print(sub_eaq_sum([5,6,-5,5,3,5,3,-2,0],8))

# find largest_sub arry with same 0's and 1's

#[0,0,1,1,1,0,0]
# -1 -2 -1 0,0
# turn 0 to -1 find the longest subarray that sum to 0

def binary_sub_same_one_zero(arr):
    pos_sum = {}
    pos_sum[0] = -1
    acc = 0
    max_len = 0
    res = []
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1
        acc += arr[i]
        if acc not in pos_sum:
            pos_sum[acc] = i
        if acc in pos_sum:
            start_idx = pos_sum[acc]
            tmp = i-start_idx
            if tmp > max_len:
                max_len = tmp
                res = [start_idx+1,i]
    return  res
print(binary_sub_same_one_zero([0,0,1,0,1,0,0]))

