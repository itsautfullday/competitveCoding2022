#Quest : Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(node : TreeNode):
            if(node == None):
                return 0
            else:
                return 1 + max(height(node.left), height(node.right))
        
        heightOfRoot = height(root)
        if(heightOfRoot == 0):
            return []
        result = [[] for _ in range(heightOfRoot)]
        traversalData = []
        traversalHelper = [(root,0)]
        while(len(traversalHelper) > 0):
            traversalData.append(traversalHelper[0])
            nodeInQuestion = traversalHelper[0][0]
            levelOfNode = traversalHelper[0][1]
            if(nodeInQuestion.left != None):
                traversalHelper.append((nodeInQuestion.left, levelOfNode + 1))
            if(nodeInQuestion.right != None):
                traversalHelper.append((nodeInQuestion.right, levelOfNode + 1))
            traversalHelper.pop(0)
        
        for treeNodeTup in traversalData:
            result[treeNodeTup[1]].append(treeNodeTup[0].val)
        
        for i in range(len(result)):
            if(i%2 == 1):
                result[i] = result[i][::-1]
            
        return result
        
        
