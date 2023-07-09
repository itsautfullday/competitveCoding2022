#Coin change max number of ways : Recurs Memoised!
class Solution:
    def count(self, coins, N, sum):
        # code here 
        minCoin = min(coins)
        
        coins = sorted(coins)
        dp = [[None for i in range(sum + 1)] for j in range(N + 1)]
        def helper(target, sizeOfArr):
            # print("Checking taregt ",target, "sizeOfArr ",sizeOfArr )
            if(target == 0):
                return 1
            if(target < minCoin):
                return -1
            if(dp[sizeOfArr][target] != None):
                return dp[sizeOfArr][target]
            res = 0
            for i in range(sizeOfArr - 1, -1, -1):
                coin = coins[i]
                if(coin > target):
                    continue
                else:
                    waysFromCoin = helper(target - coin, i + 1)
                    # print("Target ", target, " coin ", coin , " waysFromCoin ", waysFromCoin)
                    if(waysFromCoin != -1):
                        res += waysFromCoin
            if(res > 0):
                dp[sizeOfArr][target] = res
            else:
                dp[sizeOfArr][target] = -1
            return dp[sizeOfArr][target]
        result = helper(sum, N)                 
        if(result > 0):
            return result
        return 0

