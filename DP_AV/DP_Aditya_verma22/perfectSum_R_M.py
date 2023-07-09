#https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1

class Solution:
    def perfectSum(self , arr, n_size, sum):
        countof0sAtIndex = [0 for i in range(n_size)]
        count = 0
        for i in range(n_size):
            if(arr[i] == 0):
                count +=1
            countof0sAtIndex[i] = count
        
        dp = [[-1 for i in range(sum + 1)] for j in range(n_size + 1)]
        # print("Arr ", arr[0:n_size])
        def helper(n, target):
            if(target == 0):
                if(n == 0):
                    return 1 
                else:
                    return (2 ** (countof0sAtIndex[n-1]))
            if(n == 0):
                return 0
            if(dp[n][target] != -1 ):
                return dp[n][target]
            if(arr[n - 1] > target):
                val = helper(n - 1, target)
                # print("Retruning tar < arr ",target,n,arr[n-1], val)
                dp[n][target] = val % (10**9 + 7)
            else:
                valinc = helper(n - 1, target - arr[n - 1])
                valnotinc = helper(n - 1, target)
                # print("Retirong ",target, n, arr[n-1], valinc, valnotinc)
                dp[n][target] = (valinc + valnotinc) % (10**9 + 7)
            return dp[n][target] 
        
        try:
            ans = helper(n_size, sum)
            return ans
        except Exception as e:
            print(e)
            return 0
        