#https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        T = [[-1 for i in range(W + 1)] for j in range(n + 1)]
        
        for i in range(n+1):
            for j in range(W + 1):
                if(i == 0 or j == 0):
                    T[i][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1 , W + 1):
                if(wt[i - 1] > j):
                    T[i][j] = T[i-1][j]
                else:
                    T[i][j] = max(
                        val[i-1] + T[i-1][j-wt[i-1]],
                        T[i-1][j]
                        )
        return T[n][W]
        


