# from ast import List
# import math
# def minPathSum(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [math.inf] * (n + 1)
#         dp[1] = 0
#         for r in range(m):
#          for c in range(n):
#                 dp[c + 1] = min(dp[c], dp[c + 1]) + grid[r][c]
#         return dp[-1]