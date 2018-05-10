string = "1294"
base = ord('0')

for letter in string:
    ascii_val = ord(letter)
    integer = ascii_val%base
    print(integer)
