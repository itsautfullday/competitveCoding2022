#https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors
class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = {}
        def helper(floors_to_calculate, eggs):
            if floors_to_calculate == 0:
                return 0
            
            if floors_to_calculate == 1:
                return 1

            if eggs == 1:
                return floors_to_calculate # have to visit each floor from start floor to  start floor + floors_to_calculate [for 3 0 to 2]

            if (floors_to_calculate, eggs) in dp:
                return dp[floors_to_calculate, eggs]
            
            min = None
            if eggs == 2:
                for i in range(1, floors_to_calculate):
                    max_moves_for_floor = max(
                        helper(i - 1, eggs - 1), #egg broke on ith floor 
                        helper(floors_to_calculate - i, eggs) #egg didnt break ; hence n - i floors to check!
                    )
                    if not min:
                        min = max_moves_for_floor
                    elif min > max_moves_for_floor:
                        min = max_moves_for_floor
            if not min:
                print(floors_to_calculate, eggs)
            dp[floors_to_calculate, eggs]=  min + 1
            return dp[floors_to_calculate, eggs]
        return helper(n,2)

            
        
