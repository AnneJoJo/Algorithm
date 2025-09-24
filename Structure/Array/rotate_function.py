def rotate(A):
    """

    :param A: [4,3,2,1]
    :return: maximum value

    f(0) = 4*0 + 3*i + 2*2 + 1*3
    f(1) = 1*0 + 4*1 + 3*2 + 2*3  cur * (index + number) if (index+number) >= len -1 count the differ    f(2) = 2*0 + 1*1 + 4*2 + 3*3


    """
   # brute force
    res_max = 0
    l = len(A)
    i = 0
    while i < l:
        acc = 0
        for idx, v in enumerate(A):
            if idx + i < l:
                acc += v*(idx+i)
            else:
                acc += v*(idx+i-l)

        res_max = max(res_max,acc)
        i += 1


    print(res_max)

    # dp
    acc = 0
    f_zero = 0
    for i, v in enumerate(A):
        acc += v
        f_zero += i*v
    last_f = f_zero
    for k in range(1,len(A)):

        cur_f = last_f+acc-l*A[l-k]
        res_max = max(res_max,last_f+acc-l*A[l-k])
        last_f = cur_f
        


rotate([4, 3, 2, 6])