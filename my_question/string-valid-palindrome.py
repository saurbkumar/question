'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
Input: "aba"
Output: True

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

More Detail : https://leetcode.com/problems/valid-palindrome-ii/description/
'''

s = 'abqa'
def tst(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            '''
            reason of taking two variable:
            think of saurruasp
            when left = 0 and right = 8 (i.e. first iteration)
                there is mismatch so :
                    one = saurruas and two = aurruas
            '''
            part_one, part_two = s[left:right], s[left + 1:right + 1]
            return part_one == part_one[::-1] or part_two == part_two[::-1]# check the reverse of the sting with the string
        left, right = left + 1, right - 1
    return True
print tst(s)
