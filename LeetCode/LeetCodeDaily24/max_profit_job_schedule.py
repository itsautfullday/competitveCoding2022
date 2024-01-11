# Unable to solve
# note was that the way to find the correct next job was to look at the sorted endtime of find your own search time and if that existed
# Use binary search to find the next job
# Need to revisit this one
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        next_start = [[] for k in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # print("Comparing ",i,j,startTime[j],endTime[i] )
                if startTime[j] >= endTime[i]:
                    next_start[i].append(j)
        
        # print(next_start)
        dp = [None for j in range(n)]



        def helper(start):
            n = len(next_start[start])
            if n == 0:
                return profit[start]
            if dp[start]:
                return dp[start]
            max_upcoming = -1
            for i in next_start[start]:
                new_try = helper(i)
                if new_try > max_upcoming:
                    max_upcoming = new_try
    
            dp[start] = profit[start] + max_upcoming
            return dp[start]

        
            
        for i in range(n):
            dp[i] = helper(i)
        
        return max(dp)

