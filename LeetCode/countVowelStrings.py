class Solution:
    def countVowelStrings(self, n: int) -> int: 
        letToWordStart = {
            "a": ["a","e","i","o","u"],
            "e": ["e","i","o","u"],
            "i": ["i","o","u"],
            "o": ["o","u"],
            "u": ["u"],
        }

        indexMap = {
            "a":0,
            "e":1,
            "i":2,
            "o":3,
            "u":4
        }

        dp = [[-1 for i in range(6)] for j in range(n + 1)]
        

        def helper(char, count):
            if(count == 1):
                return 1
            
            
            if(dp[count][indexMap[char]] != -1):
                return dp[count][indexMap[char]] 

            res = 0
            for j in letToWordStart[char]:
                res += helper(j,count-1 )
            
            dp[count][indexMap[char]]  = res
            return dp[count][indexMap[char]] 
        

        s = 0
        for m in letToWordStart:
            s += helper(m, n)
        return s