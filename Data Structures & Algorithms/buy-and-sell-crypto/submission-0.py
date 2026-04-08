class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpft = 0
        for i in range(len(prices)-1):
            if prices[i] < max(prices[i+1:]):
                pft =  max(prices[i+1:]) - prices[i]
                if pft > maxpft:
                    maxpft = pft
        return maxpft