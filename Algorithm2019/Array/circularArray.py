def circularArrayLoop(self, nums: List[int]) -> bool:
    """
    simulate the operation 
    """
        idx = 0
        l = len(nums)
       
        for i, v in enumerate(nums):
            count = 0
            idx = i
            while True:
                if count > l:
                    break
                next_step = nums[idx]
                if next_step*nums[i] < 0:
                    break
                idx += next_step
                idx = (idx + l) % l
              
                if i == idx:
                    if count == 0:
                        print('ccc')
                        break
                    else:
                        return True
                count += 1
        
        return False