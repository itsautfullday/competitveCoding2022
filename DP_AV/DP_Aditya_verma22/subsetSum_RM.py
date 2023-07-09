#Subset sum recursive + memoised https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp = {}
        def helper(target, n):
            if(target == 0):
                # print("Helper : target ", target, " n ", n, " ret true")
                return True
            if(n == 0):
                # print("Helper : target ", target, " n ", n, " ret false")
                return False
            if(target in dp):
                return dp[target]
            if(target < arr[n-1]):
                # print("Helper : target ", target, " arr[n-1] ",arr[n-1], " ret false")
                dp[target] = helper(target, n - 1)
            else:
                dp[target] = helper(target - arr[n-1], n - 1) or helper(target, n - 1)
            return dp[target]
        return helper(sum, N)
