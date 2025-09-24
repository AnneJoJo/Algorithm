# also it's a 2d search problem, but let make it more complicated what if both
# row and col have order. they are both increasing
# there are three ways I can solve this problem
# we can check the diagonal for each use binary search if the number smaller than all of them
# it shoud be top, otherwise it should be bottom let's get the new triangle
# and do the same search again this is a good point we can try down the timeO
# to harf

# but here is the easy and optimized method similar to the diagonal method

def search_2D_matrix(matrix,target):
    row = len(matrix)
    col = len(matrix[0])

    start = 0
    end = row - 1

    while start < col and end >= 0:

        if matrix[end][start] < target:
            start += 1

        elif matrix[end][start] > target:
            end -= 1

        else:
            return  True
    return False
