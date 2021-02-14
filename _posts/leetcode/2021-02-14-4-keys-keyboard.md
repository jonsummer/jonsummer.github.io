---
title:  "leetcode-cn-651. 4 Keys Keyboard"
date:   2021-02-14
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  Imagine you have a special keyboard with the following keys:

---

# Problem

Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

    Example 1:
    Input: N = 3
    Output: 3
    Explanation: 
    We can at most get 3 A's on screen by pressing following key sequence:
    A, A, A

# Solution

- go

```go
func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
func maxA(N int) int {
	dp := make([]int, N+1)
	dp[0] = 0
	dp[1] = 1
	for i := 2; i <= N; i++ {
		dp[i] = dp[i-1] + 1
		for j := 2; j <= i; j++ {
			dp[i] = max(dp[i], dp[j-2]*(i-j+1))
		}
	}
	return dp[N]
}
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/super-egg-drop
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
