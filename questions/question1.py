from math import floor
data = raw_input().split()
data = map(int,data)
w = data[0]
m = data[1]
p = data[2]
n = data[3]
pass_req = 0
def combination(m,w,unit):
    option = []
    for k in range(unit+1):
        temp = [m+unit,w+k]
        option.append(temp)
        unit = unit-1
    return option
def findMax(options):
    all_output = []
    for option in options:
        all_output.append(option[0]*option[1])
    max_output = max(all_output)
    index = all_output.index(max_output)
    return [options[index],max_output]

no_of_candy = m*w
pass_req = pass_req + 1 
if no_of_candy == n:
    print pass_req
else:
    while no_of_candy >= n:
        pass_req = pass_req + 1
        unit = int(floor(no_of_candy/p))
        [[w,n],no_of_candy] = findMax(combination(w,m,unit))
print pass_req
