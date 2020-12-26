def consecutiveNumber(grid ,k):
    pass
# def consecutiveNumber(grid ,k):
#     """
#
#     :param grid: 2d array
#     :param k: int
#     :return: int
#     """
#     ret = []
#     if k > len(grid): return -1
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             value = grid[i][j]
#             rowCheck = dfsCheck(i, j, grid, value, 'row', 0)
#             colCheck = dfsCheck(i, j, grid, value, 'col', 0)
#             diagCheck = dfsCheck(i, j, grid, value, 'dig', 0)
#
#             if rowCheck >= k or colCheck >= k or diagCheck >= k:
#                 ret.append(value)
#
#     return min(ret) if ret != [] else -1
#
#
#
# def dfsCheck(row, col, grid, value, flag, number):
#     if row < 0 or row > len(grid)-1 or col < 0 or col > len(grid[0])-1 or grid[row][col] == '*' or grid[row][col] != value:
#         return number
#
#     grid[row][col] = '*'
#     if flag == 'row':
#         rowNum_right = dfsCheck(row,col+1, grid, value, flag, number+1)
#         rowNum_left = dfsCheck(row, col-1, grid, value, flag, number + 1)
#         grid[row][col] = value
#         return max(rowNum_right, rowNum_left)
#
#     elif flag == 'col':
#         colNum_down = dfsCheck(row+1,col, grid, value, flag, number+1)
#         colNum_up = dfsCheck(row-1, col, grid, value, flag, number + 1)
#         grid[row][col] = value
#         return max(colNum_down, colNum_up)
#
#     else:
#         diagNum_down = dfsCheck(row + 1, col + 1, grid, value, flag, number + 1)
#         diagNum_up = dfsCheck(row - 1, col - 1, grid, value, flag, number + 1)
#         diagNum_left = dfsCheck(row + 1, col - 1, grid, value, flag, number + 1)
#         diagNum_right = dfsCheck(row - 1, col + 1, grid, value, flag, number + 1)
#         grid[row][col] = value
#         return max(diagNum_down, diagNum_up, diagNum_left, diagNum_right)
#
# grid = [
#     [4,4,1,1],
#     [3,3,1,4],
#     [7,1,9,2],
#     [1,1,6,5]
# ]
# print(consecutiveNumber(grid, 4))
