# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def isGoodNode(self,root:TreeNode, max_node:int):
            if root is None:
                return
            if root.val>=max_node:
                self.count+=1
            max_node=max(max_node,root.val)
            isGoodNode(self,root.left,max_node)
            isGoodNode(self,root.right,max_node)
        isGoodNode(self,root=root,max_node=root.val)
        return self.count