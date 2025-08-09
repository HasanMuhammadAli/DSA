'''
Name: Muhammad Ali Mosin Hasan
Date: 9/8/25
Problem: 682: Baseball Game
'''

def calPoints(operations):
    """
    Calculate the total score of a baseball game based on the given operations.
    """
    stk = []
    total = 0

    for op in operations:
        if op == '+':
            score = stk[-1] + stk[-2]
            stk.append(score)
            total += score

        elif op == 'D':
            score = stk[-1] * 2
            stk.append(score)
            total += score

        elif op == 'C':
            total -= stk.pop()

        else:
            score = int(op)
            stk.append(score)
            total += score
            
    return total

# Example 1: Basic operations
print("Example 1:")
operations1 = ["5","2","C","D","+"]
result1 = calPoints(operations1)
print(f"Result: {result1}") 

print()

# Example 2: More complex operations
print("Example 2:")
operations2 = ["5","-2","4","C","D","9","+","+"]
result2 = calPoints(operations2)
print(f"Result: {result2}")


