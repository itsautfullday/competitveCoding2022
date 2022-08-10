#https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def helper(index) -> List[List[int]]:
            # print("Helper : being called with index ", index)
            if(index == 0):
                return [[nums[index]]]
            
            arraysOfPast = helper(index - 1)
            #Following from logic that for index 0 --> 1, for 1 --> 2
            lenOfArr = index
            
            lenOfArrsFromCurrentIndex = index + 1
            
            # print("Helper : lenOfArr ", lenOfArr, " lenOfArrsFromCurrentIndex ", lenOfArrsFromCurrentIndex)
            # print("Helper : arrays of the past ",arraysOfPast)
            res = []
            for arr in arraysOfPast:
                for indexOccupiedByNum in range(lenOfArrsFromCurrentIndex):
                    newArrGenerated = [-100 for i in range(lenOfArrsFromCurrentIndex)]
                    for arrPopulatorIndex in range(lenOfArrsFromCurrentIndex):
                        if(arrPopulatorIndex < indexOccupiedByNum):
                            newArrGenerated[arrPopulatorIndex] = arr[arrPopulatorIndex]
                        elif(arrPopulatorIndex == indexOccupiedByNum):
                            newArrGenerated[arrPopulatorIndex] = nums[index]
                        else:
                            newArrGenerated[arrPopulatorIndex] = arr[arrPopulatorIndex - 1]
                    # print("Helper : Array being generated ", newArrGenerated)
                    res.append(newArrGenerated)    
            return res
        
        return helper(n-1)
                            
                    
                
                
                
                
            
        
