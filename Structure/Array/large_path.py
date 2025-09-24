def large_path(x,y):
    len_x = len(x)
    len_y = len(y)
    if len_x > len_y:
        return large_path(y,x)
    overlap = []
    acc_x = 0
    acc_y = 0
    x_arr = []
    y_arr = []
    for i in range(len_x):
        acc_x += x[i]
        if x[i] in y:
            overlap.append(x[i])
            x_arr.append(acc_x)
            acc_x = 0
    x_arr.append(acc_x)
    for j in range(len_y):
        acc_y += y[j]
        if y[j] in overlap:
            y_arr.append(acc_y)
            acc_y = 0
    y_arr.append(acc_y)
    res = 0

    for idx in range(len(y_arr)):
        res += max(x_arr[idx],y_arr[idx])
    return res



x = [3,6,7,8,10,12,15,18,100]
y = [1,2,3,5,7,9,10,11,15,16,18,25,50]

print(large_path(x,y))

## 3, 7, 15, 18
## y 1 2   before 3
## x 0

## y 6 between 3 - 7
## x 5   get the larger sub

## y 8, 10, 12  between 7 - 15
## x 9,10,11

## y 16 between 15- 18
#  x  0
# y 100 after 18
# x 25 50