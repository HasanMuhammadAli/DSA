'''
Name: Muhammad Ali Mosin Hasan
Date: 1/7/25
Problem: 150: Evaluate Reverse Polish Notation
'''

def evalRPN(tokens):
    '''
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    '''
    stk = []
    for ch in tokens:
        if ch in ["+", "-", "*", "/"]:
            b, a = stk.pop(), stk.pop()
            if ch == "+":
                stk.append(a + b)
            elif ch == "-":
                stk.append(a - b)
            elif ch == "*":
                stk.append(a * b)
            elif ch == "/":
                stk.append(int(a / b))
        else:
            stk.append(int(ch))
    return stk[0]

print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))   