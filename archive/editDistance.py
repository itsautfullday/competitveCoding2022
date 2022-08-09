def main():
    s = input()
    t = input()
    s1 = list(s)
    s2 = list(t)

    m = len(s1)
    n = len(s2)

    if(abs(m-n) > 1):
        return False

    dp = [[-1 for i in range(n)] for j in range(m)]

    def helper(indexOfS1, indexOfS2):
        if(indexOfS1 < 0 and indexOfS2 < 0):
            return 0
        if(indexOfS1 <0):
            return indexOfS2 + 1
        if(indexOfS2 < 0):
            return indexOfS1 + 1
        if(dp[indexOfS1][indexOfS2] != -1):
            return dp[indexOfS1][indexOfS2]
        if(s1[indexOfS1] == s2[indexOfS2]):
            dp[indexOfS1][indexOfS2] = helper(indexOfS1 -1 , indexOfS2-1)
        else:
            s2RemovedLast = helper(indexOfS1 ,indexOfS2 -1)
            s2InsertedLast = helper(indexOfS1-1, indexOfS2)
            s2Replaced = helper(indexOfS1-1, indexOfS2-1)
            ar = [s2RemovedLast, s2InsertedLast, s2Replaced]
            dp[indexOfS1][indexOfS2]=  1 + min(ar)
        return dp[indexOfS1][indexOfS2]

    return helper(m-1, n-1) == 1