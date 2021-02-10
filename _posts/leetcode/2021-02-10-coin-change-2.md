---
title:  "leetcode-cn-518. Coin Change 2"
date:   2021-02-10
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

---
# Problem

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

    Example 1:

    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

# Solution

- cpp

```cpp
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int sz = coins.size();
        int asz = amount+1;
        if (sz==0 && amount==0){
            return 1;
        }
        if (sz==0){
            return 0;
        }
        vector<vector<int> > dp(sz+1,vector<int>(asz,0) );
        dp[0][0]=1;
        for (int i=0;i<sz;i++){
            dp[i][0]=1;
            for (int val=1;val<asz;val++){
                int tmp=0;
                if (i>0){
                    tmp+=dp[i-1][val];
                }
                if (val>=coins[i]){
                    tmp+=dp[i][val-coins[i]];
                }
                dp[i][val]=tmp;
            }
        }
        return dp[sz-1][amount];
    }
};
```

# Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/coin-change-2
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
