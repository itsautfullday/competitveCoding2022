class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bin_search(start, end, key):
            while(start <= end):
                
                mid = (start + end) // 2
                # print("start ", start, nums[start], " end ", end, nums[end], " mid ",mid,nums[mid] )
                if(nums[mid] == target):
                    return mid
                else:
                    if(nums[mid] < key):
                        start = mid + 1
                    else:
                        end = mid - 1
                        
            return - 1
        
        return bin_search(0, len(nums) - 1, target)