#https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        encountered_at_index = {}
        result = []
        len_res = 0
        n = len(nums)
        for i in range(n):
            key = str(nums[i])
            index_to_add = 0
            # print("Checking nums ", nums[i], encountered_at_index)
            if key in encountered_at_index:
                index_to_add = encountered_at_index[key] + 1

            if index_to_add >= len_res:
                result.append([])
                len_res +=1
            
            result[index_to_add].append(nums[i])
            encountered_at_index[key] = index_to_add
        return result
