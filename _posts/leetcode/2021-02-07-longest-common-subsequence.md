---
title:  "leetcode-cn-1143. Longest Common Subsequence"
date:   2021-02-06
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  Given two strings text1 and text2, return the length of their longest common subsequence.
---

# Promblem

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 If there is no common subsequence, return 0.

    Example 1:

    Input: text1 = "abcde", text2 = "ace" 
    Output: 3  
    Explanation: The longest common subsequence is "ace" and its length is 3.

# Solution

- cpp

```cpp
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int l1 = text1.size();
        int l2 = text2.size();
        vector<vector<int> >dp(l1, vector<int>(l2,0) );
        dp[0][0] = text1[0]==text2[0]?1:0;
        for (int i=1;i<l1;i++){ // j==0
            dp[i][0] = text1[i]==text2[0]?1:dp[i-1][0];
        }
        for (int j=1;j<l2;j++){ // i==0
            dp[0][j] = text1[0]==text2[j]?1:dp[0][j-1];
        }
        for (int i=1;i<l1;i++){
            for (int j=1;j<l2;j++){
                if (text1[i]==text2[j]){
                    dp[i][j] = dp[i-1][j-1]+1;
                }else{
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[l1-1][l2-1];
    }
};
```


- go

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/longest-common-subsequence
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
