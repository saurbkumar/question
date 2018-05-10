# time to slove 35.00
i,j,k = raw_input().split()
logan_day = map(str,range(int(i),int(j)+1))
k = int(k)
beautiful_days = 0
for day in logan_day:
    reverse = day[::-1]
    day = int(day)
    reverse = int(reverse)
    value = abs(day-reverse)
    if(True):
        #print value%k
        if(value % k == 0):
            beautiful_days = beautiful_days + 1
print beautiful_days
