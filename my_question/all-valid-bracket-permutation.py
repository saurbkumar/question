'''
Input : n=1
Output: {}

Input : n=2
Output: 
{}{}
{{}}

https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/
'''

def printParenthesis(string, openP, closeP):
    if(openP==0 and closeP==0):
    # all opening and closing are done
        print string
    else:
        if(openP>closeP):
            return        
        if(closeP>0):
            printParenthesis(string+'}',openP,closeP-1)  
        if(openP>0):
            printParenthesis(string+'{',openP-1,closeP)
          

n = 3

printParenthesis("", n,n)
