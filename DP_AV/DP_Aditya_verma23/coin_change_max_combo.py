class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins)
        n = len(coins)
        min_coins = min(coins)
        dp = {}
        def helper(total, last_picked_index):
            if total == 0:
                return 1
            if total < min_coins:
                return 0
            if total < coins[last_picked_index]:
                return 0
            if (total, last_picked_index) in dp:
                return dp[(total, last_picked_index)]
            ans = 0
            for i in range(last_picked_index, n):
                denom = coins[i]
                if denom > total:
                    continue
                ans += helper(total - denom, i)
            # print("Ending helper ", total, ans)
            dp[(total, last_picked_index)] = ans
            return dp[(total, last_picked_index)]
        return helper(amount, 0)
