'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.


Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

'''
Basic Idea : minPrice is the minimum price from day 0 to day i. And maxPro is the maximum profit we can get 
from day 0 to day i. How to get maxPro? Just get the larger one between current maxPro and prices[i] - minPrice.
'''
cost = [100,100,5,3,6,4]
profit = 0
min_prize = cost[0]
for index in range(1,len(cost)):
    profit = max(profit,cost[index]-min_prize)
    min_prize = min(min_prize,cost[index])
print(profit)
