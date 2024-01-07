#https://leetcode.com/problems/assign-cookies/
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        n = len(g)
        m = len(s)

        children_happy = 0
        child= 0
        for i in range(m):
            cookie = s[i]
            if child >= n:
                break
            if g[child] <= cookie:
                #child happy
                children_happy +=1
                child +=1
            else:
                #useless cookie
                pass
        return children_happy


            