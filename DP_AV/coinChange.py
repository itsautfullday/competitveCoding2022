#Have to do again
#Have to do again
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = min(coins)
        if(amount == 0):
            # print("target ", target, " res ", 0)
            return 0
        if(amount < minCoins):
            return -1
        
        dp = [None for i in range(amount + 1)]
        def helper(target):
            # print("target ", target)
            if(target == 0):
                # print("target ", target, " res ", 0)
                return 0
            
            if(target < minCoins):
                # print("target ", target, " res ", -1)
                return -1
            
            
            if(dp[target] != None):
                return dp[target] 
            
            minVal = -1
            
            for coin in coins:
                
                valForCoin = helper(target - coin)
                if(valForCoin >= 0):
                    if(minVal == -1 or valForCoin < minVal):
                        minVal = valForCoin
            if(minVal == -1):
                dp[target] = -1
            else:
                dp[target] = minVal + 1
            # print("target ", target, " res ", dp[target])
            return dp[target]
            
        return helper(amount)
                
                
        