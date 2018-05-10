input_ = "abcabcdaabb"
def maxString(input_):
    curr_str = set()
    max_len = 0
    for letter in input_:
        if letter in curr_str:
            curr_str = set(letter)
        else:
            curr_str.add(letter)
        max_len = max(len(curr_str),max_len)
    return max_len
