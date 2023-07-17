# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        def findNode(root, node, stack):
            stack.append(root)
            if(root.val == node.val):
                return stack
            else:
                if(node.val > root.val):
                    return findNode(root.right, node, stack)
                else:
                    return findNode(root.left, node, stack)
        p_path = findNode(root, p, [])
        q_path = findNode(root, q, [])

        curr_ans = root
        for i in range(min(len(p_path), len(q_path))):
            if(p_path[i].val == q_path[i].val):
                curr_ans = p_path[i]
            else:
                return curr_ans
        return curr_ans

        


            
