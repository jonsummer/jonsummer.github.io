---
title:  "leetcode-cn-剑指 Offer 03. 数组中重复的数字"
date:   2021-02-19
categories: 
  - Leetcode
tags:
  - tree
excerpt: >
  找出数组中重复的数字。

---

# Problem
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

    示例 1：

    输入：
    [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3 
     

    限制：

    2 <= n <= 100000

# Solution

-- go

```go
func findRepeatNumber(nums []int) int {
    sz:=len(nums)
    for i:=0;i<sz;i++{
        for nums[i]!=i{
            j:=nums[i]
            if j==nums[j]{
                return j
            }else{
                swap(nums,i,nums[i])
            }
        }
    }
    return -1
}

func swap(nums []int, i int,j int){
    tmp:=nums[i]
    nums[i]=nums[j]
    nums[j]=tmp
}
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
