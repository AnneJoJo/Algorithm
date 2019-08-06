from random import seed
from random import random
from random import randint
# seed random number generator

# generate some random numbers

def generate_random_number():
    print(random(), random(), random())
    rand_large = int(random()*2**10) % 100
    return rand_large

print(generate_random_number())

def generate_random_number_byPro(prob, arr):

    prob_num = [None]*100
    for i in range(len(prob)):
        r_num = prob[i]
        while r_num > 0:
            r_idx = randint(0,99)
            if prob_num[r_idx] != None:
                continue
            else:
                prob_num[r_idx] = arr[i]
                r_num -= 1
    tmp_idx = randint(0,99)
    return prob_num[tmp_idx]
print(generate_random_number_byPro([50,20,15,15],[5,2,4,1]))

# generate uniform certain numbers of list

# how to use random2 to generate random 3

# 00 --- 0
# 01 ---- 1
# 10 ------2
# 11 -------throw again
