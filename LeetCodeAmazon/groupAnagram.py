def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        res = {}
        for i in range(n):
            sortedValue = "".join(sorted(strs[i]))
            if(sortedValue not in res):
                res[sortedValue] = []
            res[sortedValue].append(strs[i])
        finalRes = [res[key] for key in res]
        return finalRes
