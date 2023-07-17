class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(s : str):
            if(s >= '0' and s <= '9'):
                return True
            if(s >= 'A' and s <= 'Z'):
                return True
            if(s >= 'a' and s <= 'z'):
                return True
            return False

        def toLower(s : str):
            diff = ord('a') - ord('A')
            if(s >= 'A' and s <= 'Z'):
                return chr(ord(s) + diff)
            return s

        real_s = []
        for char in s:
            if(not isAlphaNum(char)):
                continue
            else:
                real_s.append(toLower(char))

        return real_s == real_s[::-1]

