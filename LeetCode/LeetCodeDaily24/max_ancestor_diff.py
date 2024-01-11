# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.tree_max = -1
        def min_val(root: TreeNode):
            if root == None:
                return None
            left_min = min_val(root.left)
            right_min = min_val(root.right)
            arr = [root.val]
            if left_min != None:
                arr.append(left_min)
            if right_min != None:
                arr.append(right_min)
            return min(arr)

        def max_val(root: TreeNode):
            if root == None:
                return None
            left_max = max_val(root.left)
            right_max = max_val(root.right)
            arr = [root.val]
            if left_max != None:
                arr.append(left_max)
            if right_max != None:
                arr.append(right_max)
            return max(arr)
        
        
        def compute(root:TreeNode):
            if not root or (root.left == None and root.right == None):
                #bitch u useless
                return None
            #actual computation
            arr = [min_val(root.left), min_val(root.right), max_val(root.left), max_val(root.right)]
            # print("Computing for ", root.val,arr)
            for x in arr:
                if x != None:
                    diff = abs(root.val - x)
                    # print("Computing for ", root.val,arr, diff, self.tree_max)
                    if diff > self.tree_max:
                        self.tree_max = diff
            compute(root.left)
            compute(root.right)
        
        compute(root)
        # print(min_val(root), max_val(root))
        return self.tree_max
