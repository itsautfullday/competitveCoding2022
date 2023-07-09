#https://leetcode.com/problems/partition-equal-subset-sum/submissions/
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def isSubsetSum(Rtarget: int , Rn : int):
            dp = [[None for i in range(Rtarget + 1)] for j in range(Rn + 1)]
            def helper(target, n):
                # print("Target ", target , " size ", n, " last ", nums[n - 1])
                if(target == 0):
                    # print("isSubset returnin true tar 0")
                    return True
                if(n == 0):
                    # print("isSubset returnin false n 0")
                    return False
                # print(target, n, len(dp), len(dp[0]))
                if(dp[n][target] != None):
                    return dp[n][target]
                
                if(nums[n-1] > target):
                    dp[n][target] = helper(target , n - 1)
                else:
                    dp[n][target] = helper(target , n - 1) or helper(target - nums[n-1] , n - 1)
                return dp[n][target]
            
            return helper(Rtarget , Rn)
        
    

        n = len(nums)
        s = sum(nums)
        if(s % 2 == 1):
            return False
        return isSubsetSum(s//2, n)
        
                
            
        