from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def searchForIndexOfMax(nums : List[int], n :int) -> int:
            start = 0
            end = n - 1
            while(start <= end):
                mid = (start + end) //2
                if(mid >= n-1):
                    print("Error")
                    return -1
                else:
                    if(nums[mid + 1] < nums[mid]):
                        #found max value
                        return mid
                    else:
                        if(nums[start] > nums[mid]):
                            #left half is unsorted
                            end = mid - 1
                        else:
                            start = mid + 1
            print("Loop ended w/o finding anything")
            return -1


        def binSearch(start, end , key : int ,nums : List[int]) -> int:
            while(start <= end):
                mid = (start + end) //2 
                if(nums[mid] == key):
                    return mid
                else:
                    if(nums[mid] > key):
                        end = mid - 1
                    else:
                        start = mid + 1
            return -1
        
        n = len(nums)
        if(n == 1):
            if(nums[0] == target):
                return 0
            else:
                return -1
        else:
            if(nums[n-1] > nums[0]):
                #sorted arr
                return binSearch(0, n-1 , target, nums)
            else:
                val = searchForIndexOfMax(nums, n)
                if(target == nums[val]):
                    res = val
                else:
                    res = max(
                        binSearch(0, val,target, nums),
                        binSearch(val + 1, n - 1, target,nums)
                    )
                return res
            