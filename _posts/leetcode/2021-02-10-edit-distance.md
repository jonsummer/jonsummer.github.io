---
title:  "leetcode-cn-72. Edit Distance"
date:   2021-02-10
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

---
# Problem

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character 

  Example 1:

  Input: word1 = "horse", word2 = "ros"
  Output: 3
  Explanation: 
  horse -> rorse (replace 'h' with 'r')
  rorse -> rose (remove 'r')
  rose -> ros (remove 'e')

# Solution

- go

```go
func minDistance(word1 string, word2 string) int {
	len1 := len(word1) + 1
	len2 := len(word2) + 1

	dp := make([][]int, len1)
	for i, _ := range dp {
		dp[i] = make([]int, len2)
	}
	// dp[i][j] means word1[0..i-1],word2[0..j-1]
	for i, _ := range dp {
		for j, _ := range dp[i] {
			tmp := math.MaxInt64
			if j-1 >= 0 {
				if dp[i][j-1]+1 < tmp {
					tmp = dp[i][j-1] + 1 // insert
				}
			}
			if i-1 >= 0 {
				if dp[i-1][j]+1 < tmp { // del
					tmp = dp[i-1][j] + 1
				}
			}
			if i-1 >= 0 && j-1 >= 0 {
				if word1[i-1] == word2[j-1] { //same
					if dp[i-1][j-1] < tmp {
						tmp = dp[i-1][j-1]
					}
				} else {
					if dp[i-1][j-1]+1 < tmp { //replace
						tmp = dp[i-1][j-1] + 1
					}
				}
			}
			if i == 0 && j == 0 {
				tmp = 0
			}
			dp[i][j] = tmp
		}
	}
	return dp[len1-1][len2-1]
}

```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/edit-distance
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。