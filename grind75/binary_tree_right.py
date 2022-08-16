#https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Level order traversal with a level of a node stored with it
        #Once the next node exists and the level is changing add that node into the list
        
        
        res = []
        traversalQueue = deque()
        
        if(root == None):
            return res
        
        traversalQueue.append([root, 0])
        n = 0
        
        levels = []
        
        while(traversalQueue):
            poppedTup = traversalQueue.popleft()
            
            levels.append(poppedTup)
            popped = poppedTup[0]
            level = poppedTup[1]
            
            # print("Popped ",popped.val, level)
            n+=1

            if(popped.left != None):
                # print("Appending ",popped.left.val, level + 1)
                traversalQueue.append([popped.left, level + 1])
            
            if(popped.right != None):
                # print("Appending ",popped.right.val, level + 1)
                traversalQueue.append([popped.right, level + 1])
                
            
        for i in range(n):
            node = levels[i][0]
            lev = levels[i][1]
            
            if(i == n-1):
                res.append(node.val)
            else:
                nextLev = levels[i + 1][1]
                if(lev < nextLev):
                    # print("for node ", node.val, lev, nextLev)
                    res.append(node.val)
                    
        return res
                    
            
                
            
        
        
        
