#https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
digit = ['1','3','1','2','3','4',"5"]

table = [0]*(len(digit)+1)

table[0]=1
table[1] = 1

for index in range(2,len(digit)+1):
    if (digit[index-1] > '0'): 
			table[index] = table[index-1]
    if (digit[index-2] =='1' or (digit[index-2] == '2' and digit[index-1]<='6')):
        table[index] = table[index-2] + table[index]
