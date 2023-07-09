class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        
       
        # code here
        
        minW = min(wt)
        dp = {}
        def helper(index, capLeft):
            if(index < 0):
                return 0
            if(capLeft < minW):
                return 0
            if((index, capLeft) in dp):
                return dp[(index, capLeft)]
            
            if(capLeft < wt[index]):
                dp[(index, capLeft)] = helper(index - 1, capLeft)
            else :
                dp[(index, capLeft)] = max(
                        helper(index - 1, capLeft - wt[index]) + val[index],
                        helper(index - 1, capLeft) 
                    )
            return dp[(index, capLeft)]
            
        return helper(n - 1, W)
