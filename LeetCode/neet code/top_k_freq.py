#https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for j in nums:
            i = str(j)
            if i in frequency:
                frequency[i] +=1
            else:
                frequency[i] = 1
        ans_maker = []
        n = 0
        for num in frequency:
            n+=1
            ans_maker.append((num, frequency[num]))
        
        ans_maker = sorted(ans_maker, key= lambda x: x[1])
        print(ans_maker[n-k:n])
        return [int(x[0]) for x in ans_maker[n-k:n]]
        

        
