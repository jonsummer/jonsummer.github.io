---
title:  "leetcode-cn-剑指 Offer 06. 从尾到头打印链表"
date:   2021-02-19
categories: 
  - Leetcode
tags:
  - data structure
excerpt: >
  输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

---

# Problem

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。


    示例 1：

    输入：head = [1,3,2]
    输出：[2,3,1]
     

限制：

0 <= 链表长度 <= 10000

# Solution

-- go

```go

const MaxElem int = 10010

var stack []int = nil

func reversePrint(head *ListNode) []int {
	if stack == nil {
		stack = make([]int, MaxElem)
	}
	sp := 0
	for head != nil {
		//push
		stack[sp] = head.Val
		sp++
		head = head.Next
	}
	ret := make([]int, sp)
	k := 0
	for i := sp - 1; i >= 0; i-- {
		//pop
		ret[k] = stack[i]
		k++
	}
	return ret
}
```
# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。