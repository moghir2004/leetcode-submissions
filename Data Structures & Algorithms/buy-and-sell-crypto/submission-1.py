class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1
        maxP = 0
        while len(prices) > right:
          if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            maxP = max(maxP,current_profit)
          else:
            left = right
          right += 1
        return maxP
