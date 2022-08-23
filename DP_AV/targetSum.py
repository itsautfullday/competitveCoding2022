def findTargetSumWays(self, nums: List[int], target: int) -> int:
    n_size = len(nums)
    arr_sum = 0
    for i in range(n_size):
        arr_sum += abs(nums[i])
    
    hmap = {}
    arr_sum += abs(target)
    neg = -1 * arr_sum
    for i in range(neg, arr_sum + 1):
        hmap[i] = [-1 for i in range(n_size + 1)]
        # print("Entry added for ", i)
    
    
    
    
    def helper(n, currValue):
        if(n == 0):
            if(currValue == 0):
                return 1
            return 0
        
        else:
            if(hmap[currValue][n] != -1):
                return hmap[currValue][n]
    
            numIncludedWPlus = helper(n-1, currValue - nums[n-1])
            numIncludedWMinus = helper(n-1, currValue + nums[n-1])
            hmap[currValue][n] =  numIncludedWPlus + numIncludedWMinus
            return hmap[currValue][n]
            
    
    
    
    sol = helper(n_size, target)
    # print("Max ", self.maxCurVal, self.minCurrVal)
    return sol