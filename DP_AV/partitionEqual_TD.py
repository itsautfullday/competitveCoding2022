#https://leetcode.com/problems/partition-equal-subset-sum/submissions/
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def isSubsetSum(Rtarget: int , Rn : int):
            dp = [[None for i in range(Rtarget + 1)] for j in range(Rn + 1)]
            
            for i in range(Rtarget + 1):
                dp[0][i] = False
            for i in range(Rn + 1):
                dp[i][0] = True
                
            for i in range(1,Rn + 1):
                for j in range(1,Rtarget + 1):
                    
                    if(j < nums[i - 1]):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
            return dp[Rn][Rtarget]
            
        n = len(nums)
        s = sum(nums)
        if(s % 2 == 1):
            return False
        return isSubsetSum(s//2, n)
        
                
            
        