class Solution:
    def isValid(self, s: str) -> bool:
        closings= {
            '}':'{',
            ']':'[',
            ')':'('
        }

        openings = set(['(', '{', '['])

        from collections import deque

        stack = deque()
        for i in s:
            if(i in openings):
                stack.appendleft(i)
            else:
                if(not stack):
                    return False
                lastEl = stack.popleft()
                if(lastEl != closings[i]):
                    return False
        
        
        return not stack