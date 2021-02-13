---
title:  "leetcode-cn-1312. Minimum Insertion Steps to Make a String Palindrome"
date:   2021-02-12
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  Given a string s. In one step you can insert any character at any index of the string.Return the minimum number of steps to make s palindrome.

---

# Problem

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

    Example 1:

    Input: s = "zzazz"
    Output: 0
    Explanation: The string "zzazz" is already palindrome we don't need any insertions.

# Solution

- go

```go
func minInsertions(s string) int {
    sz:=len(s)
    if sz==0 || sz==1{
        return 0
    }
    dp:=make([][]int,sz)
    for i:=0;i<sz;i++{
        dp[i]=make([]int,sz)
    }
    for i:=sz-2;i>=0;i--{
        for j:=i+1;j<sz;j++{
            if s[i]==s[j]{
                dp[i][j]=dp[i+1][j-1]
            }else{
                dp[i][j]=min(dp[i][j-1]+1,dp[i+1][j]+1)
            }
        }
    }
    return dp[0][sz-1]
}

func min(a int, b int) int{
    if a<b{
        return a
    }else{
        return b
    }
}
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
