class Solution:
    def numSplits(self, s: str) -> int:
        r_unique = {}
        l_unique = {}

        lCount = 0
        rCount = 0
        res = 0
        n = len(s)
        for i in range(n):
            if(i == 0):
                l_unique[s[i]] = 1
                lCount +=1
            else:
                if(s[i] not in r_unique):
                    r_unique[s[i]] = 0
                    rCount +=1

                r_unique[s[i]] += 1
        
        # print("l_unique ", l_unique, " r_unique ", r_unique, "lCount", lCount, "rCount", rCount)
        
        for i in range(1, n):
            if(lCount == rCount):
                res +=1
            charMoving = s[i]
            # print("Char moving ", charMoving)

            if(r_unique[charMoving] == 1):
                rCount -=1
            r_unique[charMoving] -=1


            if(charMoving not in l_unique):
                lCount +=1
                l_unique[charMoving] = 0
            l_unique[charMoving] +=1 

        return res
            

