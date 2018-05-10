# logic - If opening bracket comes push it to stack and if closing bracket comes, just pop element to stack
# more detail here  - http://interactivepython.org/runestone/static/pythonds/BasicDS/SimpleBalancedParentheses.html#lst-parcheck1

inpt = '())()'

def checker(inpt):
    s = []
    balanced = True
    index = 0
    while index < len(inpt) and balanced:
        symbol = inpt[index]
        if symbol == "(":
            s.push(symbol)
        else:
            # if stack is empty and comes the closing bracket, then it unbalance 
            # Ex - ()(()
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
