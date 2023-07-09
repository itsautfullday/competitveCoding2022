def cutRod(price, n):
    #code here
    dp = [-1 for i in range(n + 1)]
    def helper(rod_size):
        if(rod_size <= 0):
            return 0
        if(dp[rod_size] != -1) :
            return dp[rod_size]
        mVal = -1
        
        for i in range(rod_size - 1, -1, -1):
            costForThisPart = price[i]
            lenRemaining = rod_size - 1 - i
            profit = costForThisPart + helper(lenRemaining)
            if(profit > mVal):
                mVal = profit
        dp[rod_size] = mVal
        return dp[rod_size]
    return helper(n)

print(cutRod([3, 5, 8, 9, 10, 17, 17, 20], 8))