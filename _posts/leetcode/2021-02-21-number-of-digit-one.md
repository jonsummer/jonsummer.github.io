---
title:  "leetcode-cn-233. Number of Digit One"
date:   2021-02-19
categories: 
  - Leetcode
tags:
  - tree
excerpt: >
  Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

---
# Problem

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
 

    Example 1:

    Input: n = 13
    Output: 6

# Solution

-- go

```go

import (
	"fmt"
	"math"
)

func countDigitOne(n int) int {
	if n <= 0 {
		return 0
	}
	if n < 10 {
		return 1
	}
	power := int(math.Pow10((int(math.Log10(float64(n))))))
	top := n / power
	left := n - top*power
	sum := 0
	if top == 1 {
		sum += left + 1                 // 1000~1[left] , 1 at top position
		sum += countDigitOne(left)      // 1000~1[left], 1 at left position
		sum += countDigitOne(power - 1) // 0 ~ 999
	} else {
		sum += power                        // 1xxx ~ 1999 , 1 at top position
		sum += top * countDigitOne(power-1) // 0000 ~ 999, 1000~1999, 2000~2999, [top-1]000~[top-1]999
		sum += countDigitOne(left)          // [top]000~[top][left]
	}
	return sum
}
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/number-of-digit-one
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。