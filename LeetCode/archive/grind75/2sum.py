class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper = {
        }

        for i in range(len(nums)):
            if(target - nums[i] in helper):
                return [i, helper[target - nums[i]]]
            helper[nums[i]] = i