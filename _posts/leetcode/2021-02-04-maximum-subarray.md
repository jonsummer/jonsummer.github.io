---
title:  "leetcode-cn-53. maximum-subarray"
date:   2021-02-02
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
---

# Problem

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

  Example 1:

  Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
  Output: 6
  Explanation: [4,-1,2,1] has the largest sum = 6.

# Solution

It is very similar to the longest increasing subsequence, but in this problem, subarray is continous for nums[i..j]. let us define dp[i] is maxinum sum of a subarray which is ended in nums[i].

```
dp[i] = max(  dp[i-1]+nums[i] , // take nums[i] 
              dp[i]) //  only one nums[i]
```

- cpp

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int numsSz = nums.size();
        vector<int> dp(nums.begin(),nums.end());
        int ret = dp[0];
        for (int i=1;i<numsSz;i++){
            dp[i] = max(dp[i],dp[i-1]+nums[i]);
            ret = max(ret,dp[i]);
        }
        return ret;
    }
};
```

- go

```go
func maxSubArray(nums []int) int {
    numsSz:=len(nums)
    dp:=make([]int, numsSz)
    copy(dp,nums)
    for i:=1;i<numsSz;i++{
        next:=dp[i-1]+nums[i]
        if next>dp[i]{
            dp[i]=next
        }
    }
    ret :=dp[0]
    for _ , v := range dp{
        if v>ret{
            ret = v
        }
    }
    return ret
}
```
# Reference

  来源：力扣（LeetCode）
  链接：https://leetcode-cn.com/problems/maximum-subarray
  著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。