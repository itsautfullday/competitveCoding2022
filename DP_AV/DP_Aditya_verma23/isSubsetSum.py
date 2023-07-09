class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        minVal = min(arr)
        dp= {}
        
        def helper(index, valToBeMade):
            if(valToBeMade == 0):
                return True
                
                
            if(index < 0):
                return False
            
                
            if(valToBeMade < minVal):
                return False
            
            if((index, valToBeMade) in dp):
                return dp[(index, valToBeMade)]
            
            if(arr[index] > valToBeMade):
                dp[(index, valToBeMade)] = helper(index - 1, valToBeMade)
            else:
                ansIfUsed = helper(index - 1, valToBeMade - arr[index])
                ansIfNotUsed = helper(index - 1, valToBeMade)
                dp[(index, valToBeMade)] = ansIfUsed or ansIfNotUsed
            # print("Compute for ", index, valToBeMade, dp[(index, valToBeMade)]  )
            return  dp[(index, valToBeMade)]
            
            
        return helper(N - 1, sum)
