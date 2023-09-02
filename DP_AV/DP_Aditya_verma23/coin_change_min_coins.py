class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = min(coins)
        n = len(coins)
        dp = {}
        def helper(target):
            # print(f"Calling {target}")
            if target == 0:
                return 0
            
            if target < min_coins:
                return None
            
            if target in dp:
                return dp[target]

            res = None

            for i in range(n):
                
                denom = coins[i]
                if denom > target:
                    continue
                # print(f"In {target} calling {target - denom}")
                coins_picked = helper(target - denom)
                # print(f"In {target} returning from {target - denom} {coins_picked}")
                if coins_picked == None:
                    continue
                else:
                    if res:
                        # print(f"In {target} res not none")
                        res = min(res, coins_picked + 1)
                        # print(f"In {target} res not none post {res}")
                    else:
                        # print(f"In {target} res is none")
                        res = coins_picked + 1
                        # print(f"In {target} res none post {res}")
            
            # print(f"In {target} val returned {coins_picked}")
            dp[target] = res
            return dp[target]

        res = helper(amount)
        if res == None:
            return -1
        return res
