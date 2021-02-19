---
title:  "leetcode-cn-240. Search a 2D Matrix II"
date:   2021-02-19
categories: 
  - Leetcode
tags:
  - tree
excerpt: >
  Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

---
# Problem
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

    Example 1:


    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
    Output: true

# Solution

-- go

```go
func searchMatrix(matrix [][]int, target int) bool {
    row:=len(matrix)
    if row==0{
        return false
    }
    col:=len(matrix[0])
    if col==0{
        return false
    }
    i:=0
    j:=col-1
    for true{
        if matrix[i][j]==target{
            return true
        }
        if matrix[i][j]<target{
            i++
            if !valid(i,j,row,col){
                break
            }
        }
        if matrix[i][j]>target{
            j--
            if !valid(i,j,row,col){
                break
            }
        }
    }
    return false
}

func valid(i , j , row , col int) bool{
    return i>=0 && i<row && j>=0 && j<col
}
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。