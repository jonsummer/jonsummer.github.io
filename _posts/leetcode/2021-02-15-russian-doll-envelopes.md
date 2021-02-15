---
title:  "leetcode-cn-354. Russian Doll Envelopes"
date:   2021-02-15
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

---

# Problem

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

    Example:

    Input: [[5,4],[6,4],[6,7],[2,3]]
    Output: 3 
    Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

# Solution

- go

```go
import (
    "sort"
)

func max(a int, b int) int{
    if a>b{
        return a
    }else{
        return b
    }
}
func maxEnvelopes(envelopes [][]int) int {
    sz:=len(envelopes)
    if sz==0{
        return 0
    }
    sort.Slice(envelopes, func (i int, j int) bool{
        if envelopes[i][0]<envelopes[j][0]{
            return true
        }else if envelopes[i][0]==envelopes[j][0]{
            return envelopes[i][1]>=envelopes[j][1]
        }else{
            return false
        }
    })
    dp:=make([]int, sz)
    dp[0]=1
    ret:=1
    for i:=1;i<sz;i++{
        dp[i]=1
        for j:=0;j<i;j++{
            if envelopes[i][1]>envelopes[j][1]{
                dp[i]=max(dp[i],dp[j]+1)
            }
        }
        ret=max(ret,dp[i])
    }
    return ret
}
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/russian-doll-envelopes
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
