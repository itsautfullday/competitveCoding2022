class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_seen_till_i = None
        max_profits = [0 for m in range(n)]

        for i in range(n):
            if(min_seen_till_i != None):
                max_profits[i] = max(prices[i] - min_seen_till_i, 0)

            if(min_seen_till_i == None or prices[i] < min_seen_till_i):
                min_seen_till_i = prices[i]
            
        return max(max_profits)

        