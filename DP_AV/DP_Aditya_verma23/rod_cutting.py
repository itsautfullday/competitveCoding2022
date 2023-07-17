class Solution:
    def cutRod(self, price, n):
        # code here
        dp = [0 for i in range(n + 1)]
        dp[1] = price[0]

        for i in range(n + 1):
            if (i == 0 or i == 1):
                continue
            max = -1
            for j in range(1, i + 1):
                index = j - 1
                val = price[index] + dp[i - j]
                # print("I",i,"J ",j ," index ", index, dp[j], price[index], max)
                if (val > max):
                    max = val

            # print("Setting ", i , max)
            dp[i] = max

        return dp[n]
