# https://leetcode.com/problems/coin-change/submissions/
class Solution:
    def coinChangeRecurseMemoised(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = {}
        def helper(target):
            if(target == 0):
                return 0
            if(target < coins[0]):
                return -1
            if(target in dp):
                return dp[target]
            
            minVal = -1
            for coin in coins:
                if(coin > target):
                    break
                
                coinUsedAns = helper(target - coin)
                if(coinUsedAns == -1):
                    continue
                else:
                    valCoin = coinUsedAns + 1
                    if(minVal == -1 or minVal > valCoin):
                        minVal = valCoin
            dp[target] = minVal
            return dp[target]
        
        return helper(amount)
    
    def coinChange(self, coinsGiven: List[int], amount: int) -> int:
        if(amount == 0):
            return 0
        
        coins = []
        for coin in coinsGiven:
            if(coin <= amount):
                coins.append(coin)
        
        n = len(coins)
        if(n == 0):
            return -1
        
        coins = sorted(coins)
        
        dp = [None for i in range(amount + 1)]
        
        dp[0] = 0
        
        for coin in coins:
            if(coin < amount):
                dp[coin] = 1
        
        for i in range(amount + 1):
            if(dp[i] != None):
                continue
            else:
                minValForI = -1
                for j in coins:
                    if(j > i):
                        break
                    ansJUsed = dp[i - j]
                    if(ansJUsed == -1):
                        continue
                    else:
                        ansForI = ansJUsed + 1
                        if(minValForI == -1 or minValForI > ansForI):
                            minValForI = ansForI
                dp[i] = minValForI
        
        # print(amount, dp)
        
        return dp[amount]
                
        
            
        