#User function Template for python3
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp = [[-1 for i in range(n + 1)] for j in range(W + 1)]
        # print(dp)
        def helper(w,index):
            if(w <= 0):
                return 0
            if(index >= n):
                return 0
            # print("Checking ", w, index)
            
            if(dp[w][index] != -1):
                return dp[w][index]
            
            if(wt[index] > w):
                dp[w][index] = helper(w,index + 1)
            else:
                #otherwise consider what happens if you pick this index
            
                valIfIndexPicked = helper(w - wt[index],index + 1) + val[index]
                valIfIndexNotPicked = helper(w,index + 1)
                dp[w][index] = max(valIfIndexPicked, valIfIndexNotPicked)
                # print("Setting w ",w," index ", index, dp[w][index])
            return dp[w][index]
        
        return helper(W, 0)
        
        
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends