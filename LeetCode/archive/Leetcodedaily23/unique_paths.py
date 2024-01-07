class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def helper(x, y):
            if x == m - 1 or y == n - 1:
                return 1
            if (x,y) in dp:
                return dp[(x,y)]
            left_ans = 0
            down_ans = 0
            if x < m-1:
                #robot can go right
                left_ans = helper(x + 1, y)
            if y < n - 1:
                #robot can go down
                down_ans = helper(x, y + 1)
            
            dp[(x,y)] = left_ans + down_ans
            return dp[(x,y)]
        
        return helper(0,0)


        
