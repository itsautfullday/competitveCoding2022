#https://leetcode.com/problems/maximum-length-of-repeated-subarray/
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp = {}
        # def LCS_ends_at(n , m):
        #     if n == 0 or m == 0:
        #         return 0
        #     if (n,m) in dp:
        #         return dp[(n,m)]
        #     if nums1[n-1] == nums2[m - 1]:
        #         dp[(n,m)] = LCS_ends_at(n - 1, m - 1) + 1
        #     else:
        #         dp[(n,m)] = 0
            
        #     return dp[(n,m)]

        
        n = len(nums1)
        m = len(nums2)
        max = -1
        dp = [[None for i in range(m+1)] for j in range(n+1)]
        for i in range(m + 1):
            dp[0][i] = 0
        
        for i in range(n + 1):
            dp[i][0] = 0


        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                
                if dp[i][j] > max :
                    max = dp[i][j]

        return max

            
        
