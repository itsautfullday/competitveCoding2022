# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, st: List[str]) -> int:
        stack = []
        stack_count = 0

        def push(i):
            stack.append(int(i))
 
            # print("Push ",stack)
        
        def pop():
            el = stack[-1]
            stack.pop()
            # print("Popped ",el,stack)
            return el
        
        def peek():
            return stack[-1]
        
        tokens = set(['+', '-', '*', '/'])
        

        for el in st:
            # print("parsing el ", el)
            if el not in tokens:
                #is a number
                #push to stack
                # print("pushing el ", el)
                push(el)
            else:
                el1 = pop()
                el2 = pop()
                ans = 0
                if el == '+':
                    ans = el1 + el2
                elif el == '-':
                    ans = el2 - el1
                elif el == '/':
                    # print(el2, el1, el2/el1)
                    ans =int(el2 / el1)
                else:
                    ans = el2 * el1
                push(ans)
        
        return stack[0]

        
        
        
