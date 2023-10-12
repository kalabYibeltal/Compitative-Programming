# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(int)
   
        def dfs(node,depth):
            nonlocal dic
            if not node:
                return 
            if not node.left and not node.right:
                dic[depth] += node.val
            
            dfs(node.left,depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root,0)
        
        return dic[max([key for key in dic])]