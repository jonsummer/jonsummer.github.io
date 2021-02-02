---
title:  "leetcode-cn-300. Longest Increasing Subsequence"
date:   2021-02-02
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  Given an integer array nums, return the length of the longest strictly increasing subsequence.

---
## Problem

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

    Example 1:

    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

## Solution

Dynamic Programming Algorithm. We will define dp[i] which is the longest length of increasing subsequence that ends with nums[i]. It means that the last element of choosing subsequence must be nums[i]. Then considering, 

    dp[i] = max{ dp[i], 
            dp[i-1]+1 if nums[i] > nums[i-1],
            dp[i-2] if nums[i] > nums[i-2], 
            ...}


- cpp

```cpp
#include <algorithm>
#include <vector>

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int numsSz = nums.size();
        vector<int> dp(numsSz,1) ; // default dp[1..n]=1
        for (int i=0; i<numsSz; i++){
            for (int j=i+1; j<numsSz; j++){
                if (nums[j]>nums[i]){
                    dp[j] = max(dp[j],dp[i]+1);
                }
            }
        }
        int ret = *max_element(dp.begin(),dp.end());
        return ret;
    }
};

```

- go

```go
func lengthOfLIS(nums []int) int {
    numsSz := len(nums)
	dp := make([]int, numsSz)
	for i:=0;i<numsSz;i++{
		dp[i]=1
	}
    for i:=0;i<numsSz;i++{
        for  j:=i+1;j<numsSz;j++{
            if nums[j]>nums[i]{
                newVal := dp[i]+1
                if newVal>dp[j]{
                    dp[j] = newVal;
                }
            }
        }
    }
    ret:=1
    for i:=0;i<numsSz;i++{
        if dp[i]>ret{
            ret=dp[i]
        }
    }
    return ret;
}
```




## Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。