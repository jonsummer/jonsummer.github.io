---
title:  "leetcode-cn-416. Partition Equal Subset Sum"
date:   2021-02-06
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

---
# Problem

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 
    Example 1:

    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Solution

- cpp

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(),nums.end(),0);
        if (sum%2==1){ // odd
            return false;
        }
        int target = sum/2;
        int sz = nums.size();
        int tsz = target+1;
        vector<vector<bool> > dp(sz,vector<bool>(tsz,false) );
        if (nums[0]<tsz){
            dp[0][nums[0]] = true;
        }
        for (int i=1;i<sz;i++){
            for (int val=0;val<=tsz;val++){
                if (val<nums[i]){
                    dp[i][val] = dp[i-1][val];
                }else{
                    dp[i][val] = dp[i-1][val]||dp[i-1][val-nums[i]];
                }
            }
        }
        return dp[sz-1][target];
    }
};
```
- go

```go
func canPartition(nums []int) bool {
    sum:=0
    for _,v :=range nums{
        sum+=v
    }
    if sum%2!=0{
        return false
    }
    target := sum/2
    tsz := target+1
    sz :=len(nums)
    dp :=make([][]bool, sz)
    for i:=0;i<sz;i++{
        dp[i] = make([]bool, tsz)
    }
    if nums[0]<tsz{
        dp[0][nums[0]]=true
    }
    for i,v :=range nums{
        if i==0{
            continue
        }
        for val:=0;val<tsz;val++{
            if val<v{
                dp[i][val] = dp[i-1][val]
            }else{
                dp[i][val] = dp[i-1][val]||dp[i-1][val-v]
            }
        }
    }
    return dp[sz-1][target]
}
```
# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。.
