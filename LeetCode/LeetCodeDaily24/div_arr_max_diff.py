#https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = []
        for i in range(0,n,3):

            diff_1 = abs(sorted_nums[i] - sorted_nums[i+1])
            diff_2 = abs(sorted_nums[i] - sorted_nums[i+2])
            diff_3 = abs(sorted_nums[i+1] - sorted_nums[i+2])
            if diff_1 > k or diff_2 > k or diff_3 > k:
                return []
            ans.append([sorted_nums[i], sorted_nums[i+1], sorted_nums[i+2]])
        return ans

        
        
