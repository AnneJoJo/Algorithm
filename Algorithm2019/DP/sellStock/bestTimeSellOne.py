class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        maxVal = 0
        for i in range(len(prices)-1):
            if prices[i+1] < prices[buy]:
                buy = i + 1
            else:
                maxVal = max(maxVal, prices[i+1]-prices[buy])

        return maxVal



