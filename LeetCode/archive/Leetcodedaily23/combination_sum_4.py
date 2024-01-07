#https://leetcode.com/problems/combination-sum-iv/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        min_coins = min(nums)
        nums = sorted(nums)
        dp = {}
        def helper(target):
            # print("Calling for ", target)
            if target == 0:
                return 1
            if target < min_coins:
                return 0
            if target < 0:
                return 0
            
            if target in dp:
                return dp[target]
            

            ans = 0
            

            for denom in nums:
                if denom > target:
                    break
                
                # print("Ading call for ", target, target - denom)
                denom_ways = helper(target - denom)
                # print("Returning call for ", target, target - denom, denom_ways)
                ans += denom_ways
                
                
            
            dp[target] = ans
            return dp[target]

        return helper(target)

        
