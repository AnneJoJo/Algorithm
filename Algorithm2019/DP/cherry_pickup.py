"""
This is a very interesting problem
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  -1]]

 you can go twice to pick the maximum value avoid 0 and -1

 twice greedy is not a good choice, because optimum in partial is not the optimum in global.
 we could hypothesize there are two people pick up the value at the same time and if they go to the same place, always keep the largest.

"""
def cherry_pickup(grid):

    N = len(grid)
    memo = [[[None]*N for _ in range(N)] for _ in range(N)] # 3D dp memo

    def dp(x1,y1,y2):
        x2 = x1 + y1 - y2
        if x1 == N or x2 == N or y1 == N or y2 == N or grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return -float('inf')
        elif x1 == y1 == N-1: # until hit the destination return the value bottom up (dfs) we could also using iterative top to down
            print(x1,y1)
            return grid[x2][y2]
        elif memo[x1][y1][y2] != None:
            return memo[x1][y1][y2]

        else:
            res = max(dp(x1+1,y1,y2),dp(x1,y1+1,y2),dp(x1+1,y1,y2+1),dp(x1,y1+1,y2+1))
            if y1 != y2:
                res += grid[x1][y1]
            res += grid[x2][y2]

        memo[x1][y1][y2] = res
        return  res
    return max(0,dp(0,0,0))
grid = [[0, 1, -1],[1, 0, -1],[1, 1,  1]]

print(cherry_pickup(grid))

