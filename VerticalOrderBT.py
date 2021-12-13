
#https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        hash=dict()
        def dfs(root,x,y):
            if root:
                hash[y]=hash[y] if  y in hash else []
                hash[y].append((x,root.val))
                dfs(root.left,x+1,y-1)
                dfs(root.right,x+1,y+1)
        dfs(root,0,0)
        return list(map(lambda x:list(map(lambda y : y[1],sorted(hash[x]))),sorted(hash)))
        