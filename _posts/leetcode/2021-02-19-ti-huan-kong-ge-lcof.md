---
title:  "leetcode-cn-剑指 Offer 05. 替换空格"
date:   2021-02-19
categories: 
  - Leetcode
tags:
  - tree
excerpt: >
  请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

---

# Problem
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000

# Solution

-- go

```go
func replaceSpace(s string) string {
    // first round
    spaceCount:=getSpaceCount(s)
    sz:=len(s)
    newSz:=sz+spaceCount*2
    str:=make([]byte,newSz)
    last:=sz-1
    i:=newSz-1
    for i>=0{
        if last>=0 && s[last]==' '{ //space
            str[i]='0'
            i--
            str[i]='2'
            i--
            str[i]='%'
            i--
            last--
        }
        for last>=0 && s[last]!=' '{ // not space
            str[i]=s[last]
            i--
            last--
        }
    }
    return string(str)
}
func getSpaceCount(s string) int {
	cnt:=0
	for _,v:=range s{
		if v==' '{
			cnt++
		}
	}
	return cnt
}
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

