def longest_con_seq(nums):
    # [100,0,2,1,3,4,200]

    if nums == [] or len(nums) == 0: return 0

    num_s = set(nums)

    res = 0
    for each in num_s:

        cur_val_lr = each
        while cur_val_lr in num_s:
            cur_val_lr += 1
        cur_val_sm = each  # -1

        while cur_val_sm in num_s:
            cur_val_sm -= 1

        res = max(res, each - cur_val_sm, cur_val_lr - each)

    return res

longest_con_seq([2,0,2,1,4,3,1,0])

def conse_seq(arr):
    nums = set(arr)
    res = 0
    for each in nums:
         if each - 1 not in nums:
             cur_next = each
             while cur_next in nums:
                 cur_next += 1
             res = max(res, cur_next-each)
    return res