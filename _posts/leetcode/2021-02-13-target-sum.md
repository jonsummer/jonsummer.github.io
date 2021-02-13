---
title:  "leetcode-cn-494. Target Sum"
date:   2021-02-13
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

---

# Problem

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

    Example 1:

    Input: nums is [1, 1, 1, 1, 1], S is 3. 
    Output: 5
    Explanation: 

    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3

    There are 5 ways to assign symbols to make the sum of nums be target 3.

# Solution

- go

```go
func findTargetSumWays(nums []int, S int) int {
	sz := len(nums)
	dp := make([]map[int]int, sz)
	for i := 0; i < sz; i++ {
		dp[i] = make(map[int]int)
	}
	dp[0][nums[0]] = 1
	dp[0][-nums[0]] += 1 // add for nums[0] is 0, +0, -0 are two ways
	for i := 1; i < sz; i++ {
		for k, v := range dp[i-1] {
			dp[i][k+nums[i]] += v
			dp[i][k-nums[i]] += v
		}
	}
	ret, has := dp[sz-1][S]
	if has {
		return ret
	} else {
		return 0
	}
}
```
# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/target-sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。