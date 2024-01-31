# https://leetcode.com/problems/daily-temperatures/?envType=daily-question&envId=2024-01-31
class Solution:
    
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0 for i in range(n)]

        # from collections import deque LEARN ALL DEQUE FUNCTIONS
        # Also all list and heap fucntions

        temp_encountered_stack = []
        t_count = 0
        for i in range(n-1, -1, -1):
            if t_count != 0:
                #in this scenario we need to check the stack
                while t_count != 0 and temp_encountered_stack[-1][0] <= temp[i]:
                    # print("Encountered ", temp_encountered_stack[-1][0],temp[i], "hence popping" )
                    temp_encountered_stack.pop()
                    t_count -=1 
                
                if t_count != 0:
                    #we have met the element that is closest and is larger
                    #t_count is its index from the back : hence if n = 7 and t_count = 3, its index = n - t_count (in case of 7 - 1 = 6)
                    # hence the diff is index - i
                    # print("temo count not 0 ", temp_encountered_stack[-1][0],temp[i], "hence popping" , temp_encountered_stack[-1][1] - i)
                    ans[i] = temp_encountered_stack[-1][1] - i
                
            temp_encountered_stack.append((temp[i], i))
            t_count = t_count + 1

            # print(temp_encountered_stack)
            
    
        return ans
                
        

        
                

        
