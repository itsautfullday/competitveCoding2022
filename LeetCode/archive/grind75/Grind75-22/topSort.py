#https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numcourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sort
        outNodesPerNode = {}
        indegreeOfEachNode = [0 for i in range(numcourses)]
        coursesCompleted = 0
        
        for tupleOfCourses in prerequisites:
            prev = tupleOfCourses[1]
            after = tupleOfCourses[0]
            if(prev not in outNodesPerNode):
                outNodesPerNode[prev] = []
            outNodesPerNode[prev].append(after)
            indegreeOfEachNode[after] += 1
            
        
        
        from collections import deque
        
        queOfZeros = deque()
        for course in range(numcourses):
            if(indegreeOfEachNode[course] == 0):
                queOfZeros.append(course)
                
        while(queOfZeros):
            valOfCourse = queOfZeros.popleft()
            coursesCompleted += 1
            if(valOfCourse in outNodesPerNode):
                coursesComingOutOfCourse = outNodesPerNode[valOfCourse]
                for course in coursesComingOutOfCourse:
                    indegreeOfEachNode[course] -= 1
                    if(indegreeOfEachNode[course] == 0):
                        queOfZeros.append(course)
        
        
        if(numcourses == coursesCompleted):
            return True
        return False
            
        
        
                
            
            
        
        
