#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # cannot use the division algo
        # must run in o(n)
        n = len(nums)
        prefix_multiply = [1 for i in range(n)]
        suffix_multiply = [1 for i in range(n)]

        # ans = [1 for i in range(n)]

        #prefix_calcn
        for i in range(1,n):
            prefix_multiply[i] = nums[i-1] * prefix_multiply[i-1]
        
        # print(prefix_multiply)
        
        for i in range(n-2, -1, -1):
            suffix_multiply[i] = nums[i+1] * suffix_multiply[i+1]
        
        # print(suffix_multiply)

        ans = [prefix_multiply[i] *  suffix_multiply[i] for i in range(n)]
        return ans

        
