---
title:  "leetcode-cn-236. Lowest Common Ancestor of a Binary Tree"
date:   2021-02-19
categories: 
  - Leetcode
tags:
  - tree
excerpt: >
  Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

---

# Problem
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 

    Example 1:


    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

# Solution

-- go

```go
/**
 * Definition for TreeNode.
 * type TreeNode struct {
 *     Val int
 *     Left *ListNode
 *     Right *ListNode
 * }
 */
 func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
     if root==nil{
         return nil
     }
     if root.Val==p.Val || root.Val==q.Val{
         return root
     }
     left:=lowestCommonAncestor(root.Left,p,q)
     right:=lowestCommonAncestor(root.Right,p,q)
     if left==nil && right==nil{
         return nil
     }
     if left!=nil && right!=nil{
         return root
     }
     if left==nil && right!=nil{
         return right
     }
     if left!=nil && right==nil{
         return left
     }
     //nothing at here
     return nil
}
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。