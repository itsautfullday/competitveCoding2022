class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def helper(ind, currTarget):
            if(currTarget == 0 and ind == n):
                return 1
            if(ind >= n):
                return 0
            if((ind, currTarget) in dp):
                return dp[(ind, currTarget)]
            else :
                dp[(ind, currTarget)] = helper(ind + 1 , currTarget - nums[ind]) + helper(ind + 1 , currTarget + nums[ind]) 
            return dp[(ind, currTarget)]
        return helper(0, target)
            
