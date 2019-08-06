# so given a 2D matrix the items in the matrix are placed as increasing order
# find target number as fast as you can
# apperently, it's like a sorted array, the only thing we need to solve is 2D trick.
# since the order follows one direction. We can flat 2d matrix linearly, which means convert
# the 2d to 1d, then we can use binary search to solve this problem


def search_2D_matrix(matrix,target):

    row = len(matrix)
    col = len(matrix[0])
    total = row*col - 1

    start = 0

    while start <= total:
        mid = (start+total)//2

        if matrix[mid/col][mid%col] == target:
            return True
        elif matrix[mid/col][mid%col] < target:
            start = mid + 1

        else:
            total = mid - 1


    return  False