class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp ={}

        def helper(index_1, index_2):
            if index_1 == -1 or index_2 == -1:
                return 0
            if (index_1, index_2) in dp:
                return dp[(index_1, index_2)]
            #Pick the last index of both the strings
            if text1[index_1] == text2[index_2]:
                dp[(index_1, index_2)] = helper(index_1 -1, index_2 -1) + 1
            #in this scenario LCS(m, n) = LCS(m-1, n-1) + 1
            else:
                #In this scenario LCS(m,n) = max(LCS(m-1, n) , LCS(m, n-1)
                dp[(index_1, index_2)] = max(
                    helper(index_1, index_2 -1),
                    helper(index_1 - 1, index_2)
                )
            return dp[(index_1, index_2)]
        return helper(m-1, n-1)
