# Matrxi rotation, with extra space
'''
Idea is rows become colums in opposite order, as seen below first row become first column in opposite order
Input
 1  2  3
 4  5  6
 7  8  9

Output:
 3  6  9 
 2  5  8 
 1  4  7 

Input:
 1  2  3  4 
 5  6  7  8 
 9 10 11 12 
13 14 15 16 

Output:
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13
'''

# Matrix Rotation without extra space
https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

"""
An N x N matrix will have floor(N/2) square cycles. For example, a 4 X 4 matrix will have 2 cycles. 
The first cycle is formed by its 1st row, last column, last row and 1st column. 
The second cycle is formed by 2nd row, second-last column, second-last row and 2nd column.
"""
