# You are given an integer array prices where prices[i] is the price of a given stock on
# the ith day. Design an algorithm to find the maximum profit.You may complete at most k
# transactions.
# #
# Example
# 1:
#
# Input: k = 2, prices = [2, 4, 1]
# Output: 2
# Explanation: Buy
# on
# day
# 1(price=2) and sell
# on
# day
# 2(price=4), profit = 4 - 2 = 2.
# Example
# 2:

# Input: k = 2, prices = [3, 2, 6, 5, 0, 3]
# Output: 7
# Explanation: Buy
# on
# day
# 2(price=2) and sell
# on
# day
# 3(price=6), profit = 6 - 2 = 4.
# Then
# buy
# on
# day
# 5(price=0) and sell
# on
# day
# 6(price=3), profit = 3 - 0 = 3.
"""
当日卖出之后可以再买
负值是买入
正值是卖出， 两数和为收益 max——diff 如果为正就是截止这一天上一次交易所赚的钱 ，包括比较若购入今天的股票会如何，值减小就放弃购入，维持最小的那个买入点
第一次交易的上一次是第0次交易，没有收入 即为0， 多次交易后， 如果当天卖完再买是负值，就不会立刻再买，反正max valule 会滤掉 负值
默认每天都在发生交易
如果持有股票 必须先卖之后才能再买
因为都是正数，全部加法计算，maintain 最大值即可

"""


class Stock(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        dif -3  -2  -2 -2 0 0
            -3 -2   -2  -1 4
            3   2   6   5  0 3
        0   0   0   0   0  0 0
        1   0   0   4   4  4 4
        2   0   0   4   4  4 7


        dif -3  -2  -2 -2 -2 -2
            -3 -2   -2  -2 1 0
            3   2   6   8  5 6
        0   0   0   0   0  0 0
        1   0   0   4   6  6 6
        2   0   0   4   6  6 7

        """

        if k >= len(prices) // 2:
            return sum(
                x - y
                for x, y in zip(prices[1:], prices[:-1])
                if x > y)

        if prices == []:
            return 0
        col = len(prices)
        dpT = [ [0] * col for _ in xrange(k + 1) ]


        for i in range(1 , k +1):
            max_diff = -prices[0]
            for j in range(1 ,col):
                dpT[i][j] = max(dpT[i][j-1] ,prices[j] + max_diff ) #sell
                max_diff = max(max_diff, dpT[i-1][j] -prices[j]) #maxprofit of last transaction at the same day. buy if larger

        print(dpT)
        return dpT[k][col - 1]

