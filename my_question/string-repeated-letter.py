'''
When we need to find out the repeated letter in the string and
the string is not sorted
'''
s = 'Java'
table = dict()
for letter in s:
    # will find out, whether letter is in dictionary or not
    try:
        table[letter] = table[letter] + 1
    except:
        table[letter] = 1
for letter in table.keys():
    if table[letter]>1:
        print letter
'''
When the string is sorted like " aabccccde"
--> output is a,c
'''
s = "aabccccde"
word = ''
for index,letter in enumerate(s):
    if index==0 or s[index]!=s[index-1]:
        if len(word)>1:
            print word[-1]
        word = s[index]
    else:
        word = word + s[index]
