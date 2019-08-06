# 321 123
# 123  132
# 213  231
# 132   213
# let check the number from the back to the front if arr[-1] < arr[-2] keep moving to the front
# otherwise let's check all the elements after the larger one including the larger one and find the smallest number swap

def next_permutation(num):
    """
    
    :param num: list 
    :return: 
    """

    for i in range(len(num))[::-1]:

        if i>0 and num[i-1] < num[i]:
            tmp_min = num[i]
            smaller_index = 0
            for j in range(i,len(num)):

                if num[j] <= tmp_min and num[j] > num[i-1]:
                    tmp_min = num[j]
                    smaller_index = j

            num[i-1],num[smaller_index] = num[smaller_index],num[i-1]
            num = num[:i] + num[i:][::-1]
            return num

    return num[::-1]

print(next_permutation([4,4,8,7,3,2]))