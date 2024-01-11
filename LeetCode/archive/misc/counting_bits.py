# https://leetcode.com/problems/counting-bits/
class Solution:
    def countBits(self, n: int) -> List[int]:
        power_2s = set([2 ** i for i in range(30)])
        result_arr = [0 for i in range(n + 1)]

        result_arr[0] = 0

        last = 0
        for i in range(1, n + 1):
            if i in power_2s:
                result_arr[i] = 1
                last = i
            else:
                result_arr[i] = 1 + result_arr[i - last] 
            
                
            
        
        return result_arr
        
