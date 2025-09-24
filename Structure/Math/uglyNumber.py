


def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    n nth 2 , 3 , 5
    6 15 10 30

    simulate and brtue force
    """
    primeSet = [2, 3, 5]
    start = 2
    ret = [1]
    while True:
        if len(ret) == n:
            break
        cur = start
        flag = False
        for each in primeSet:
            while cur > 1:
                if cur % each == 0:
                    cur = cur // each
                    flag = True
                else:
                    flag = False
                    break
        if (flag):
            ret.append(start)
        start += 1

    return ret[-1]


print(nthUglyNumber(1000))
