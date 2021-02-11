---
title:  "leetcode-cn-516. Longest Palindromic Subsequence"
date:   2021-02-10
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

---
# Problem

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

  Example 1:
  Input:

  "bbbab"
  Output:
  4
  One possible longest palindromic subsequence is "bbbb".

# Solution

- go

```go
func longestPalindromeSubseq(s string) int {
	sz := len(s)
	dp := make([][]int, sz)
	for i, _ := range dp {
		dp[i] = make([]int, sz)
	}
	for i, _ := range dp {
		dp[i][i] = 1
	}
	for i := sz - 2; i >= 0; i-- {
		for j := i + 1; j < sz; j++ {
			if s[i] == s[j] {
				dp[i][j] = dp[i+1][j-1] + 2
			} else {
				tmp := dp[i+1][j]
				if tmp < dp[i][j-1] {
					tmp = dp[i][j-1]
				}
				dp[i][j] = tmp
			}
		}
	}
	return dp[0][sz-1]
}

```
# Reference

  来源：力扣（LeetCode）
  链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
  著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
