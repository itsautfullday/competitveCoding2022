#1387. Sort Integers by The Power Value
#The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:
# if x is even then x = x / 2
# if x is odd then x = 3 * x + 1

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def helper(x):
            # print("Helper being called ", x)
            if x == 1:
                return 0
            if x in res:
                return res[x]
            if x % 2 == 0:
                res[x] = 1 + helper(x/2)
            else:
                res[x] = 1 + helper((3 * x) + 1)
            return res[x]


        res = {}
        ls = [i for i in range(lo, hi + 1)]

        # for i in ls:
        #     print(helper(i))
        
        final_res = sorted(ls , key= lambda x : helper(x))
        # for keys in res:
        #     print("For ", keys, " val ", res[keys])
        # print(final_res)

        return final_res[k-1]
        
        
