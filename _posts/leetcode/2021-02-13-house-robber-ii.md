---
title:  "leetcode-cn-213. House Robber II"
date:   2021-02-13
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

---

# Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

    Example 1:

    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Solution

- go

```go
func rob(nums []int) int {
    sz:=len(nums)
    if sz==0{
        return 0
    }
    if sz==1{
        return nums[0]
    }

    dp:=make([]int,sz)
    //rob 0, but not sz-1
    dp[0]= nums[0]
    dp[1]= max(nums[1],dp[0])
    for i:=2;i<sz-1;i++{
        dp[i]=max(nums[i]+dp[i-2],dp[i-1])
    }
    robFirst:=dp[sz-2]
    //rob last, not first
    dp[0]=0
    dp[1]=nums[1]
    for i:=2;i<sz;i++{
        dp[i]=max(nums[i]+dp[i-2],dp[i-1])
    }
    robLast:=dp[sz-1]
    ret:=max(robFirst,robLast)
    return ret
}

func max(a int, b int) int{
    if a>b{
        return a
    }else{
        return b
    }
}
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/house-robber-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。