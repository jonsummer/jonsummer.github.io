---
title:  "leetcode-322: Coin Change"
date:   2021-02-01
categories: 
  - Leetcode
tags:
  - dp
excerpt: >
  You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
  You may assume that you have an infinite number of each kind of coin.
---

## Problem

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

    Example 1:

    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

## Solution

It can be solved by Dynamic Programming (DP) algorithm. Basiclly, the problem meets the following criterias.

1. The best strategy for the giving amount, DP[amount] is based on the 
   
    min{ DP[amount-Coins[0]], ... ,DP[amount-Coins[i]]}

2. The DP[amount] is only determined by vector Coins and a `small amount`

3. The DP[X] will be used several times when calculated DP[amount]

The following code will be accepted. But several details should be handled carefully.

1. If amount is zero, then return 0
2. If any coin in coins is more than amount, we should filter it out
3. The MaxAmount should be bigger than amount a lot, but not close to MAX_INT, since it will be overflow when sum them together.

I have used cpp lambda to filter useless coins.

- CPP

```cpp
#include <limits>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    const int MaxAmount = 10000;
public:
    int coinChange(vector<int>& coins, int amount) {
        int INF = amount+MaxAmount; // max value for min
        int dpSz = amount+1;
        vector<int>dp(dpSz, INF);
        dp[0]=0; // 0 coin for 0 amount
        // filter , value of coin should not be great than amount
        coins.erase(
            remove_if(coins.begin(),coins.end(), [amount](int val){ return val>amount;}),
            coins.end()
        );
        for (int i=0; i<amount; i++ ){
            int coinsSz = coins.size();
            for (int j=0;j<coinsSz;j++){
                int next = i+coins[j]; // big coins[j] will be overflow
                if (next<dpSz){
                    dp[next] = min(dp[next], dp[i]+1); // MAX_INT will be overflow 
                }
            }
        }
        int ret = dp[amount]==INF ? -1:dp[amount];
        return ret;
    }
};
```

- JAVA

```java
class Solution {
    private final int MaxAmount = 10000;
    public int coinChange(int[] coins, int amount) {
        int INF = amount+MaxAmount;
        int dpSz = amount+1;
        int[] dp = new int[dpSz];
        for (int i=0;i<dpSz;i++){
            dp[i] = INF;
        }
        dp[0]=0;
        int coinsSz = coins.length;
        // filter
        for (int i=0;i<coinsSz;i++){
            if (coins[i]>amount){
                coins[i]=-1;
            }
        }
        for (int i=0; i<amount; i++ ){
            for (int j=0;j<coinsSz;j++){
                if (coins[j]>0){
                    int next = i+coins[j]; // big coins[j] will be overflow
                    if (next<dpSz){
                        dp[next] = Math.min(dp[next], dp[i]+1); // MAX_INT will be overflow 
                    }
                }
            }
        }
        int ret = dp[amount]==INF ? -1:dp[amount];
        return ret;
    }
}
```

## Reference

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/coin-change
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。