# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s = 0
        
        def process(node : TreeNode):
            nonlocal s
            if(node == None):
                return
            if(node.val % 2 == 0):
                if(node.left != None):
                    left = node.left
                    if(left.left != None):
                        s += left.left.val
                    if(left.right != None):
                        s += left.right.val

                if(node.right != None):
                    right = node.right
                    if(right.left != None):
                        s += right.left.val
                    if(right.right != None):
                        s += right.right.val
            

        def preOrder(node):
            if(node == None):
                return
            process(node)
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return s
            
            