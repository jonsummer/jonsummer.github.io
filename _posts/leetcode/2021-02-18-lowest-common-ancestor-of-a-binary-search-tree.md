---
title:  "leetcode-cn-235. Lowest Common Ancestor of a Binary Search Tree"
date:   2021-02-18
categories: 
  - Leetcode
tags:
  - tree
excerpt: >
  Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.


---

# Problem
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 

  Example 1:


  Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
  Output: 6
  Explanation: The LCA of nodes 2 and 8 is 6.


# Solution

-cpp

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val < q->val){
            return lcaBTS(root,p,q);
        }else{
            return lcaBTS(root,q,p);
        }
    }
    TreeNode* lcaBTS(TreeNode* root, TreeNode* lo, TreeNode* hi){
        if (root->left==NULL && root->right==NULL){ //leaf
            return root;
        }else{
            if (root->val == lo->val || root->val == hi->val){ 
                return root;
            }
            if (root->val<lo->val){ // right side
                return lcaBTS(root->right,lo,hi);
            }
            if (root->val>hi->val){ // left side
                return lcaBTS(root->left,lo,hi);
            }
            if (root->val>lo->val && root->val<hi->val){ // lca found
                return root;
            }
            // nothing else
        }
        //nothing here
        return root;
    }
};
```

# Reference

  来源：力扣（LeetCode）
  链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree
  著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
