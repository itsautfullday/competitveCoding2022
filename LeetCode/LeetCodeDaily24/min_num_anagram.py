# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arr_s = [0 for i in range(26)]
        arr_t = [0 for i in range(26)]
        n = len(s)
        for index in range(n):
            char_s = ord(s[index]) - ord('a') 
            char_t = ord(t[index]) - ord('a') 
            arr_s[char_s] +=1
            arr_t[char_t] +=1
        
        count = 0
        for i in range(26):
            count += abs(arr_s[i] - arr_t[i])
        return count // 2
        