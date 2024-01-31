# https://leetcode.com/problems/determine-if-string-halves-are-alike/
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a_count = 0
        b_count = 0
        letters = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        a_counter, b_counter = 0, len(s) - 1
        while(a_counter < b_counter):
            if s[a_counter] in letters:
                a_count +=1
            if s[b_counter] in letters:
                b_count +=1
            a_counter +=1
            b_counter -=1
        
        return a_count == b_count