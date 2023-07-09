class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if(i == 0 or j == 0):
                    dp[i][j] = 0
        max = -1
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                if(S1[i-1] == S2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                
                if(dp[i][j] > max):
                    max = dp[i][j]
        
        return max