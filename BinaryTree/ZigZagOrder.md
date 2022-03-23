# Binary Tree Zigzag Level Order Traversal

[Practice Link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal)

**Code:** 

```java
class Solution {
    
    public void dfs(TreeNode root,int level,List<List<Integer>> ans){
            
            if(root==null)
                return;
        
            if (ans.size() < level + 1) {
			  ans.add(new ArrayList<>());
		    }
        
            if (level % 2 == 1) 
                ans.get(level).add(0, root.val);
                
            else 
                ans.get(level).add(root.val);
		
        
            dfs(root.left,level+1,ans);
            dfs(root.right,level+1,ans);
            
           }
                
    
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        
         List<List<Integer>> ans= new ArrayList<>();
        
         dfs(root,0,ans);
        
         return ans;
        
    }
}

```