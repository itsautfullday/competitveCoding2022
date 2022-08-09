def twoSum(self, nums: List[int], target: int) -> List[int]:
        setOfNumbersSeen = {}
        n = len(nums)
        for i in range(n):
            val = nums[i]
            if((target - val) in setOfNumbersSeen):
                return [i, setOfNumbersSeen[target-val]]
            else:
                setOfNumbersSeen[val] = i

