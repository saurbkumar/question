'''
https://leetcode.com/problems/min-cost-climbing-stairs/
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to 
reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Solution

This is relation
dp[i]=cost[i]+min(dp[i-1],dp[i-2])
'''
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
table = [0]*len(cost)
table[0] = cost[0]
table[1] = cost[1]
for index in range(2,len(cost)):
    table[index] = cost[index] + min(table[index-1],table[index-2])
print min(table[len(cost)-1],table[len(cost)-2])
