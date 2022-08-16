#Subset sum Top down https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        t = [[None for i in range(sum + 1)] for j in range(N + 1)]
        
        for i in range(N+1):
            for j in range(sum + 1):
                if(i == 0):
                    t[i][j] = False
                if(j == 0):
                    t[i][j] = True
                    
        for i in range(1,N+1):
            for j in range(1, sum + 1):
                if(arr[i-1] > j):
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = t[i-1][j] or t[i-1][j - arr[i-1]]
        return t[N][sum]
                
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends