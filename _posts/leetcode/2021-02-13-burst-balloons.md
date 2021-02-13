---
title:  "leetcode-cn-312. Burst Balloons"
date:   2021-02-12
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

---

# Problem

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

    Example 1:

    Input: nums = [3,1,5,8]
    Output: 167
    Explanation:
    nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
    coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# Solution

- go

```go
func maxCoins(nums []int) int {
	sz := len(nums)
	if sz == 0 {
		return 0
	}
	if sz == 1 {
		return nums[0]
	}
	vals := make([]int, sz+2)
	for i := 0; i < sz; i++ {
		vals[i+1] = nums[i]
	}
	vals[0] = 1
	vals[sz+1] = 1
	sz += 2
	dp := make([][]int, sz)
	for i := 0; i < sz; i++ {
		dp[i] = make([]int, sz)
	}
	for i := sz - 2; i >= 0; i-- {
		for j := i + 2; j < sz; j++ {
			bouns := 0
			for k := i + 1; k < j; k++ {
				tmp := dp[i][k] + dp[k][j] + vals[i]*vals[k]*vals[j]
				if tmp > bouns {
					bouns = tmp
				}
			}
			dp[i][j] = bouns
		}
	}
	return dp[0][sz-1]
}
```

# Refrence

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/burst-balloons
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。