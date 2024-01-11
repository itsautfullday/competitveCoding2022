# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        bfsQ = deque()
        bfsQ.append((root, 0))
        s = 0
        maxLev = -1
        
        while(bfsQ):
            elPopped, level = bfsQ.popleft()
            
            if(level > maxLev):
                s = elPopped.val
                maxLev = level
            elif(level == maxLev):
                s += elPopped.val
            else:
                print("Error this should not happen")
            # print("Popped from q ",elPopped.val, level, s, maxLev )
            if(elPopped.left != None):
                bfsQ.append((elPopped.left, level + 1))
            if(elPopped.right != None):
                bfsQ.append((elPopped.right, level + 1))
        

        return s
                
