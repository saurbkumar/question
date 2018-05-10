'''
All pattern is like for s = 'aabccdddefgggh'
-> output is a,aa,b,c,cc,d,dd,e,f,g and so
'''
s = 'aabccdddefgggh'
for index,letter in enumerate(s):
  if index == 0 or s[index-1]!=letter:
    # this will give the single letter like a,b,c and so
    word = letter
  else:
    # this will give the repeated letter in the sting
    # like aa,dd,ddd,gg,ggg and so
    word = word + letter
  print word
  
  
'''
  If just want the largest repeated string pattern, then it would be like below,
  -> output is aa,cc,ddd,ggg
'''
s = 'aabccdddefgggh'
word = ""
for index,letter in enumerate(s):
  if index == 0 or s[index-1]!=letter:
    if len(word)>1:
        print word
    word = letter
  else:
    word = word + letter
  
 
