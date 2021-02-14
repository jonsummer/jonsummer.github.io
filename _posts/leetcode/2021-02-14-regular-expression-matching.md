---
title:  "leetcode-cn-10. Regular Expression Matching"
date:   2021-02-14
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

---

# Problem

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

    Example 1:

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

# Solution

- go 

```go
func isMatch(s string, p string) bool {
	s = s + "#"
	p = p + "#"
	lenS := len(s)
	lenP := len(p)
	dp := make([][]bool, lenS+1)
	for i := 0; i <= lenS; i++ {
		dp[i] = make([]bool, lenP+1)
	}
	dp[lenS][lenP] = true
	for i := lenS - 1; i >= 0; i-- {
		for j := lenP - 1; j >= 0; j-- {
			res := false
			if s[i] == p[j] || p[j] == '.' { // match
				if j+1 < lenP && p[j+1] == '*' {
					if j+2 <= lenP {
						res = res || dp[i][j+2] // zero
					}
					if i+1 <= lenS {
						res = res || dp[i+1][j] // one more
					}
				} else {
					res = dp[i+1][j+1]
				}
			} else { // not match
				if j+1 < lenP && p[j+1] == '*' {
					if j+2 <= lenP {
						res = dp[i][j+2] // zero
					}
				} else {
					res = false
				}
			}
			dp[i][j] = res
		}
	}
	return dp[0][0]
}

```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/regular-expression-matching
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。