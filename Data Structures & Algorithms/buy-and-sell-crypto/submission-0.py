class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2 = 0, 1
        maxP = 0

        while p2 < len(prices):
            if prices[p2] > prices[p1]:
                profit = prices[p2] - prices[p1]
                maxP = max(maxP, profit)
            else:
                p1 = p2
            p2 += 1
        
        return maxP