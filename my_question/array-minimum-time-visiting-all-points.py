'''
https://leetcode.com/problems/minimum-time-visiting-all-points/

On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.

Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

Input: points = [[3,2],[-2,2]]
Output: 5
'''

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cost = 0
            
        for index in  range(len(points)-1):
            xchg = abs(points[index][0] - points[index+1][0])
            ychg = abs(points[index][1] - points[index+1][1])
            cost = cost + max(xchg,ychg)
        return cost
