#https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[-1 for j in range(i + 1)] for i in range(numRows)]
        
        for i in range(1, numRows + 1):
            number_of_els = i
            for index in range(number_of_els):
                if index == 0 or index == number_of_els - 1:
                    res[i - 1][index] = 1
                else:
                    res[i - 1][index] = res[i - 2][index-1] + res[i - 2][index]
        return res
        
