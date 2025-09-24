# Given a list of integers nums and an integer k, return the length of the longest increasing subsequence with at least k odd numbers.
#
# Constraints
#
# Example 1
# Input
#
# nums = [10, 12, 14, 3, 5, 6]
# k = 2
# Output
#
# 3

# from collections import defaultdict
#
#
# class Solution:
#     def solve(self, nums, k):
#         lens = [defaultdict(int) for _ in nums]
#         for i, n in enumerate(nums):
#             lens[i][n & 1] += 1
#
#         for i in range(len(nums)):
#             is_odd = nums[i] & 1
#             for j in range(i):
#                 if nums[j] >= nums[i]: continue
#                 for odd_count, length in lens[j].items():
#                     lens[i][odd_count + is_odd] = max(lens[i][odd_count + is_odd], length + 1)
#         print(lens)
#         ans = 0
#         for d in lens:
#             for odd_count, length in d.items():
#                 if odd_count >= k and length > ans: ans = length
#         return ans


# class SolutionB:
#     def solve(self, nums, k):
#         N = len(nums)
#         dp = [[0] * (k + 1) for _ in range(N)]
#
#         for i in range(N):
#             if nums[i] % 2 == 0:
#                 dp[i][0] = 1
#             else:
#                 dp[i][min(1, k)] = 1
#         print(dp,'one')
#         for i in range(N):
#             for j in range(i - 1, -1, -1):
#                 if nums[i] > nums[j]:
#                     for l in range(k + 1):
#                         if dp[j][l] > 0:
#                             dp[i][l] = max(dp[i][l], dp[j][l] + 1)
#                         if nums[i] % 2 == 1 and l > 0:
#                             if dp[j][l - 1] > 0:
#                                 dp[i][l] = max(dp[i][l], dp[j][l - 1] + 1)
#
#         print(dp)
#         ans = 0
#         for d in dp:
#             ans = max(ans, d[k])
#         return ans
#
# s = SolutionB()
# print(s.solve([4,5],1))
#
# print( 0 == True)

class Solution:
    def dfs_check_place(self, grid, x, y, row, col, N):
        if grid[x][col] == 'X' or grid[row][y] == 'X':
            return False
        ret1, ret2 = True, True
        if col < N-1:
            for r in range(col,N):
                ret1 = self.dfs_check_place(grid, x, y, row, col+1, N)
                if not ret1:
                    print("ret1")
                    return False

        if row < N-1:
            for c in range(row,N):
                ret2 = self.dfs_check_place( grid, x, y, row+1, col, N)
                if not ret2:
                    return False

        return ret1 and ret2



    def solve(self, matrix):
        # Write your code here
        def set_zero(matrix):
            for n in range(len(matrix)):
                for m in range(len(matrix[0])):
                    if matrix[n][m] == "X":
                        matrix[n][m] = 0
        N = len(matrix)
        count = 0

        for s in range(N):
            print(matrix,'see')
            if matrix[0][s] == 0:
                matrix[0][s] = "X"
                if self.canPlace(matrix,N):
                    count += 1
                set_zero(matrix)

        print(count)


    def canPlace(self,matrix, NN):
        for i in range(1, len(matrix)):
            for k in range(len(matrix[0])):
                if (matrix[i][k]) == 0:
                    if i == 1 and k == 1:
                        print("---->>>>>>>>>>")
                        print(self.dfs_check_place(matrix, i, k, 0, 0, NN))
                    if self.dfs_check_place(matrix, i, k, 0, 0, NN):
                        print(i,k)
                        matrix[i][k] = "X"

        print(matrix,'matrix')
        print (NN,'hinn')
        return  NN == 0



matrix = [[0, 1, 0],
[0, 0, 0],
[0, 0, 0]]

s =Solution()
s.solve(matrix)
