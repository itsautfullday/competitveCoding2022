# User function Template for python3
class Solution:
    def minDifference(self, arr, n):
        # code here
        s = sum(arr)
        dp = {}

        def helper(prev, index):
            #  print("starting helper ", prev , index)
            if (index > n - 1):
                return abs(s - (2 * prev))

            if ((prev, index) in dp):
                return dp[(prev, index)]

            diff_used = helper(prev + arr[index], index + 1)
            diff_not_used = helper(prev, index + 1)
            # print("Checking index ", index,arr[index] ," diff_used ",diff_used, "diff_not_used", diff_not_used)
            dp[(prev, index)] = min(
                diff_used,
                diff_not_used
            )

            return dp[(prev, index)]
        return helper(0, 0)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minDifference(arr, N)
        print(ans)

# } Driver Code Ends
