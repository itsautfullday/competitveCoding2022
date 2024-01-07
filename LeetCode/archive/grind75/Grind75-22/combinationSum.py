#https://leetcode.com/problems/combination-sum/submissions/
class Solution:    
    def combinationSum(self, candidates: List[int], realTarget: int) -> List[List[int]]:
        minCandidate = min(candidates)
        dp = {}
        def helper(target) -> List[List[int]]:
            # print("Helper : target ",target)
            if(target < minCandidate):
                # print("Helper : target ",target, " minCand ", minCandidate, " ret ", [])
                return []
            
            if(target in dp):
                # print("Helper : dpify ",target, dp[target])
                return dp[target]
            
            res = []
            resMap = set()
            for candidate in candidates:
                if(candidate > target):
                    # print("Helper : target ",target, " candidate ", candidate, " ret ", [])
                    continue
                else:
                    if(target - candidate == 0):
                        # print("Helper : target ",target, " candidate ", candidate, " ret ", [])
                        soln = [candidate]
                        rep = str(sorted(soln))
                        if(rep not in resMap):
                            res.append(soln)
                            resMap.add(rep)
                    else:
                        ls = helper(target - candidate)
                        # print("Helper : target ",target, " candidate ", candidate, " ls ", ls)
                        if(len(ls) > 0):
                            for rsoln in ls:
                                # print("Helper : target ",target, " candidate ", candidate, " appedning ", soln, candidate)
                                soln = rsoln.copy()
                                soln.append(candidate)
                                rep = str(sorted(soln))
                                if(rep not in resMap):
                                    res.append(soln)
                                    resMap.add(rep)
            
            dp[target] = res
            # print("Helper : target ",target, res)
            # print(dp)
            return res
        return helper(realTarget)
