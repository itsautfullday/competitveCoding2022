def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    # Write your code here
    # print(n,m,s1,s2)
    dp = {}

    def helper(n: int, m: int) -> str:
        if n == 0 or m == 0:
            return ""
        if (n,m) in dp:
            return dp[(n,m)]
        if s1[n-1] == s2[m-1]:
            dp[(n,m)] = helper(n-1, m-1) + "" + s1[n-1]
            return dp[(n,m)]
        
        s1d = helper(n,m-1)
        s2d = helper(n-1,m)
        l1 = len(s1d)
        l2 = len(s2d)
        if l1 > l2:
            dp[(n,m)]= s1d
        else:
            dp[(n,m)] = s2d
        return dp[(n,m)]
    
    res = helper(n,m)
    # print("OP : ",res)
    return res