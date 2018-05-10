a = 'abcd'
b = 'cdabcdab'
'''
the minimum number of times A has to be repeated such that B is a substring of it
'''
# question detail - https://leetcode.com/problems/repeated-string-match/description/

# find the lower bound, repetation not going to be less than that
lower_bound = int(float(len(b))/len(a))
# now the number of repetation should not be more then 2
#just try with a as above and b='cdabcdabcdab'
for i in range(2):
    if b in a*(lower_bound+i):
        print(lower_bound+i)
        break
# more on answer - https://leetcode.com/problems/repeated-string-match/discuss/108090 
