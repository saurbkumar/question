# Details here
# https://www.geeksforgeeks.org/power-set/

string = "ABC"
length = len(string)
for index in range(2**length):
    temp_binary = bin(index)[2:]
    binary = (length-len(temp_binary))*"0"+temp_binary
    print(binary)
    result = []
    for pos,bit in enumerate(binary):
        if bit=="0":
            result = result + []
        else:
            result = result + [string[pos]]
    print(["".join(result)])
