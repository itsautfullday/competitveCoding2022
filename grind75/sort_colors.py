#https://leetcode.com/problems/sort-colors/solution/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        
        n = len(nums)
        
        for i in nums:
            if(i == 0):
                count_0 +=1
            elif(i == 1):
                count_1 +=1
            else:
                count_2 +=1
        
        for i in range(n):
            if(count_0 > 0):
                nums[i] = 0
                count_0 -=1
                continue
            if(count_1 > 0):
                nums[i] = 1
                count_1 -=1
                continue
            if(count_2 > 0):
                nums[i] = 2
                count_2 -= 1
                continue
        
                
                
            
            
