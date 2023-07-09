#https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def __init__(self):
        self.last = None
        self.isBST = True
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.last = None
        self.isBST = True
        
        def inOrder(root: TreeNode):
            if(root == None):
                return
            inOrder(root.left)
            if(self.last == None or (root.val > self.last)):
                self.last = root.val
                # print("Changing last to ",self.last)
            else:
                self.isBST = False
                # print("Changing isBST to ",self.isBST)
            
            inOrder(root.right)
            
        inOrder(root)
        return self.isBST
