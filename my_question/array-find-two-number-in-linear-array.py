'''
Given an array of n unique integers where each element in the array is in
range [1, n]. The array has all distinct elements and size of array is (n-2).
Hence Two numbers from the range are missing from this array. Find the two 
missing numbers.

Idea: use n*(n+1)/2 to find out the total sum 
now subtract it from the array sum. Result is sum of the number that need to 
find out. 
To get those two numbers : two method
first try every combination - > O(n)
second use binary search to find out those element, to do binary search first 
take the average of the result that we got above, then one number is less or equal 
to the avg and other is greater.
So again first find out the sum till the average using avg(avg+1)/2 and then
add array till the average number index. and subtract both of them to get the first number
Input  : arr[] = {1, 3, 5, 6}
Output : 2 4

Input : arr[] = {1, 2, 4}
Output : 3 5

Input : arr[] = {1, 2}
Output : 3 4
'''
data = [1,3,5,6]
n = 6
