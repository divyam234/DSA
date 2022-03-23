# Boundary Traversal Binary Tree

## Intuition

![Solution](https://lh4.googleusercontent.com/I5V2oP6krQzwGUoXASv3vBVYpD_kDAMYWpjfxjbOddY08pWjgZ4nVPfc74Zg63pVUg8XI98-cB0ui9oAcr-FZmcVMqALsMHMJoOj6WZXbaCVo4xZ6d3lEGrFDwVAGHbf07P9jYju)


[Practice Link](https://www.codingninjas.com/codestudio/problems/boundary-traversal_790725)

**Code:** 

```java
import java.util.*;

class TreeNode {
    int data;
    TreeNode left;
    TreeNode right;

    TreeNode(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }

}

public class  BoundaryTraversal {

    static Boolean isLeaf(TreeNode root) {
        return (root.left == null) && (root.right == null);
    }

    static void leftBoundary(TreeNode root,ArrayList<Integer> ans){
        if(root==null || isLeaf(root))
            return;


        ans.add(root.data);

        if (root.left!=null){
            leftBoundary(root.left,ans);
        }

        else if (root.right!=null)
            leftBoundary(root.right,ans);
    }

    static void rightBoundary(TreeNode root,ArrayList<Integer> ans){
        if(root==null || isLeaf(root))
            return;

        if (root.right!=null){
            rightBoundary(root.right,ans);
        }
        else if (root.left!=null)
            rightBoundary(root.left,ans);

        ans.add(root.data);
    }

    static void leafTreeNodes(TreeNode root,ArrayList<Integer> ans){
        if(root==null)
            return;

        if(isLeaf(root))
            ans.add(root.data);

        leafTreeNodes(root.left,ans);
        leafTreeNodes(root.right,ans);
    }

    public static ArrayList<Integer> traverseBoundary(TreeNode root){

        ArrayList<Integer> ans= new ArrayList<>();

        if (!isLeaf(root)) ans.add(root.data);

        leftBoundary(root.left,ans);
        leafTreeNodes(root,ans);
        rightBoundary(root.right,ans);

        return ans;
    }

    public static void main(String[] args) {

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.left.right = new TreeNode(4);
        root.left.left.right.left = new TreeNode(5);
        root.left.left.right.right = new TreeNode(6);
        root.right = new TreeNode(7);
        root.right.right = new TreeNode(8);
        root.right.right.left = new TreeNode(9);
        root.right.right.left.left = new TreeNode(10);
        root.right.right.left.right = new TreeNode(11);

        ArrayList < Integer > boundaryTraversal;
        boundaryTraversal =  traverseBoundary(root);

        System.out.println("The Boundary Traversal is : ");
        for (Integer integer : boundaryTraversal) {
            System.out.print(integer + " ");
        }

    }
}

```