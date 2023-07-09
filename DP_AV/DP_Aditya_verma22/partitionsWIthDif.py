#https://www.codingninjas.com/codestudio/problems/partitions-with-given-difference_3751628?leftPanelTab=1
from typing import List


def countPartitions(n_size: int, d: int, arr: List[int]) -> int:
    # write your code here
    max_target = (sum(arr) + d)
    
    if(max_target % 2 != 0):
        return 0
    
    dp = [[-1 for i in range(n_size + 1)] for j in range(max_target + 1)]
    
    countof0sAtIndex = [0 for i in range(n_size)]
    count = 0
    for i in range(n_size):
        if(arr[i] == 0):
            count +=1
        countof0sAtIndex[i] = count
        
    
    def countOfSubsets(target :int , n : int):
        if(target == 0):
            if(n == 0):
                return 1
            else:
                return (2 ** (countof0sAtIndex[n-1]))
        if(n == 0):
            return 0
        if(dp[target][n] != -1):
            return dp[target][n]
        if(arr[n-1] > target):
            dp[target][n] = countOfSubsets(target , n - 1) % (10**9 + 7)
        else:
            dp[target][n] = countOfSubsets(target , n - 1) + countOfSubsets(target - arr[n-1] , n - 1) % (10**9 + 7)
        return dp[target][n]
    
    return countOfSubsets(max_target // 2, n_size) % (10**9 + 7)
    