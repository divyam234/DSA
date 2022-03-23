# Boundary Traversal Binary Tree

## Intuition

![Solution](https://media.geeksforgeeks.org/wp-content/cdn-uploads/lca.png)


[Practice Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

**Code:** 

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        if(root ==null || root==p || root== q)
            return root;
            
        
         TreeNode left= lowestCommonAncestor(root.left, p, q);
         TreeNode right=lowestCommonAncestor(root.right, p,q);
        
        return left == null ?  right : right == null ? left : root;
        
    }
}

```