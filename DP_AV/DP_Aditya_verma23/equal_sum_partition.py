class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if(s % 2 != 0):
            #if s == odd cannot be partioned into 2
            return False

        minVal = min(nums)
        dp = {}
        
        def subsetSum(sumToBeMade, indexInList) -> bool:
            if(sumToBeMade == 0):
                # in this case we don't need to look for more elements
                return True
            if(sumToBeMade < minVal):
                return False
            if(indexInList >= n):
                #ran out of elements to search from
                return False
            
            if((sumToBeMade, indexInList) in dp):
                return dp[(sumToBeMade, indexInList)]
            valAtCurrent = nums[indexInList]
            if(sumToBeMade < valAtCurrent):
                dp[(sumToBeMade, indexInList)] = subsetSum(sumToBeMade , indexInList + 1)
            else:
                dp[(sumToBeMade, indexInList)] = subsetSum(sumToBeMade -  valAtCurrent, indexInList + 1) or subsetSum(sumToBeMade, indexInList + 1)
            

            return dp[(sumToBeMade, indexInList)]

        
        return subsetSum(s//2, 0)
