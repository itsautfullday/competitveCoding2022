# https://leetcode.com/problems/sequential-digits/?envType=daily-question&envId=2024-02-02
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def genSeq(d, ans):
            if d > 9:
                return
            first = []
            num_add = []
            
            for i in range(1, d+1):
                first.append(str(i))
                num_add.append(str(1))

            
            first = int(''.join(first))
            num_add = int(''.join(num_add))
            ans.append(first)

            for i in range(10 - d - 1):
                if i < 0:
                    break
                ans.append(ans[-1] + num_add)
        
        dig_low = len(str(low))
        low_first = int(str(low)[0])

        dig_high = len(str(high))
        high_first = int(str(high)[0])

        ans_1 = []
        ans = []

        for i in range(dig_low, dig_high + 1):
            genSeq(i, ans_1)
        
        for i in ans_1:
            if i < low or i > high:
                continue
            ans.append(i)
        return ans
