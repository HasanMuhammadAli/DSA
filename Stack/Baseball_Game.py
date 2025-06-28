'''
Name: Muhammad Ali Mosin Hasan
Date: 28/6/25
Problem: 682: Baseball Game
'''

def calPoints(operations):
    """
    Calculate the total score of a baseball game based on the given operations.
    
    The function processes a list of operations where:
    - An integer represents a score that gets added to the record
    - '+' represents adding the sum of the previous two scores
    - 'D' represents doubling the previous score
    - 'C' represents invalidating the previous score (removing it)
    
    Args:
        operations (List[str]): A list of strings representing game operations
        
    Returns:
        int: The total sum of all valid scores in the record
        
   
    """
    stk = []

    for op in operations:
        if op == '+':
            stk.append( stk[-1] + stk[-2] )
        elif op == 'D':
            stk.append( stk[-1] * 2 )
        elif op == 'C':
            stk.pop()
        else:
            stk.append(int(op))
            
    return sum(stk)

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


