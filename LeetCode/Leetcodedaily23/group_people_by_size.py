#https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
class Group:
        def __init__(self, limit):
            self.limit = limit
            self.persons = []
            self.count = 0

        def can_add(self):
            return self.count < self.limit
        
        def add(self, index):
            self.count +=1
            self.persons.append(index)

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_to_group = {}
        res = []
        n = len(groupSizes)

        for i in range(n):
            group = groupSizes[i]

            if str(group) not in size_to_group:
                size_to_group[str(group)] = Group(int(group))
            
            group_obj:Group = size_to_group[str(group)] 
            if group_obj.can_add():
                group_obj.add(i)
            else:
                res.append(group_obj.persons)
                    

                size_to_group[str(group)] = Group(int(group))
                group_obj:Group = size_to_group[str(group)]
                group_obj.add(i)


        
        for el in size_to_group:
            group_obj:Group = size_to_group[el]
            res.append(group_obj.persons)
        

        return res


        
