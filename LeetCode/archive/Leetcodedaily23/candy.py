#https://leetcode.com/problems/candy/
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        dp = [None for i in range(n)]
        
        def helper(index):
            # print("Computing ", index)
            if dp[index]:
                # print("Retiurning as dp exists  ", index, dp[index])
                return dp[index]

            pre, nex = None, None
            if index != 0 and index != n - 1:
                pre, nex = index - 1, index + 1

            elif index == 0:
                nex = index + 1
            else:
                pre = index - 1
            
            # print("Indexes check ", index, pre, nex)
            
            lesser_neigh = []
            for neigh in (pre, nex):
                if neigh == None:
                    continue
                # print(index, neigh, ratings[neigh],ratings[index])
                if ratings[neigh] < ratings[index]:
                    lesser_neigh.append(neigh)

            # print("for index ", index, " less_n ", lesser_neigh)
            
            if len(lesser_neigh) == 0:
                dp[index] = 1
                return dp[index]

            maximum = -1
            for neigh in lesser_neigh:
                ans_neigh = helper(neigh)
                if ans_neigh > maximum:
                    maximum = ans_neigh
            
            dp[index] = maximum + 1
            return dp[index]
        
        res = 0
        for i in range(n):
            res += helper(i)
            # print(dp)

        
        return res
            

            
                    



        
