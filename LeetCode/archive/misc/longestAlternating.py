class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1 for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if j - 1 < 0:
                    continue
                # print("For i ",i,j,"comparing nums[j] ",nums[j], "nums[j-1]", nums[j-1],(j - (i-1)),(-1 ** (j - (i-1))), pow(-1, (j - (i-1)))) 
                
                if nums[j] - nums[j-1] == (pow (-1, j - (i-1))):
                    count[i] += 1
                else:
                    break
        
        m = max(count)
        if m == 1:
            return -1
        return m