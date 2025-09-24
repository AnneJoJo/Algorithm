import collections

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        def isReachable(stones, curPos, k):
          
            if (stones[curPos] + k ) in stones[curPos+1:]:
                return True

            return False
        def dfs(stones, curPos, memo, k):
            if k < 0:
                return False
            if curPos == len(stones)-1:
            
                return True

            for j in range(k-1, k+2):
                
                if not isReachable(stones, curPos, j) or j == 0:
                    continue
                oldPos = curPos
                curPos = stones.index(stones[curPos] + j)
          
                ret = dfs(stones, curPos, memo, j)
                if ret: return ret
                curPos = oldPos

            return False
        if stones[0] + 1 != stones[1]:
            return False
        return dfs(stones, 1, [], 1)
    

# dp array

def jumpFog(stones):
    """
    [0,1,3,5,6,8,12,17]
    dp: [0, 1, 2, 2, 3, 3, 4, 5]
    {0: set([0]), 1: set([1]), 2: set([2]), 3: set([2]), 4: set([1, 3]),
    5: set([2, 3]), 6: set([4]), 7: set([5])}))

    tmpGap: expect steps we need to jump
    i: current stone position
    k: last stone position
    memo: how many jump from last to this i stone
    check tmpGap-1) in memo[j] or tmpGap in memo[j] or (tmpGap+1) in memo[j] to see
    if there is a stone between current and previous ???
    maintain the lagest steps inner stone we might still use to jump like
    5 -> 8 
    this is a 6 between 6 [2] steps to 8 5 [3] steps to 8, we need 3 
    
    
}
    
    """
    memo = collections.defaultdict(set())
    dp = [0]*len(stones)
    memo[0].add(0)
    k = 0
    for i in range(1, len(stones)):
        while dp[k]+1 < stones[i] - stones[k]: # if step 1 dosen't land the stone bump up k
            k+=1
        for j in range(k, i):
            tmpGap = stones[i] - stones[j]
            if (tmpGap-1) in memo[j] or tmpGap in memo[j] or (tmpGap+1) in memo[j]:
                memo[i].add(tmpGap)
                dp[i] = max(dp[i],tmpGap) 
                
    return dp[-1] > 0
    
    #top down
class Solution(object):
    def canCross(self, stones):
        seen = set()
        stoneSet = set(stones)
        end = stones[-1]
        stack = [(0, 0)]
        while len(stack) > 0:
            loc, steps = stack.pop()
            if (loc, steps) in seen:
                continue
            seen.add((loc, steps))
            if loc == end:
                return True
            elif loc < end:
                for i in range(steps-1, steps+2):
                    if i <= 0:
                        continue
                    if loc + i in stoneSet:
                        stack.append((loc+i, i))
        return False
    