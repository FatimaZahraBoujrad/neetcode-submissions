# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.verifyAncestor(root,float('-inf'),float('inf'))
    def verifyAncestor(self,root,min_ans,max_ans):
        if root is None:
            return True
        left,right=True,True
        if root.val<=min_ans or root.val>=max_ans:
            return False
        if  root.left:
           
                left= self.verifyAncestor(root.left,min_ans,root.val)
           
        if root.right:
            
                right= self.verifyAncestor(root.right,root.val,max_ans)
           
        return left and right