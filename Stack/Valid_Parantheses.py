'''
Name: Muhammad Ali Mosin Hasan
Date: 29/6/25
Problem: 20: Valid Parantheses
'''

def isValid(s):
    """
    Check if the given string contains valid parantheses.
    
    The function uses a stack to keep track of opening parantheses and ensures that they are closed in the correct order.
    """
    hashmap = { ')':'(', ']':'[', '}':'{'}
    stk = []

    for c in s:
        if c not in hashmap:
            stk.append(c)
        else:
            if not stk:
                #executes only if stk is empty
                return False
            else:
                popped = stk.pop()
                if popped != hashmap[c]:
                    return False

    return not stk # return true if stk empty

# Test cases

# Test case 1: Valid parentheses - simple case
test1 = "()"
print(f"Test 1: '{test1}' -> {isValid(test1)}")  # Expected: True

# Test case 2: Valid parentheses - mixed types
test2 = "()[]{}"
print(f"Test 2: '{test2}' -> {isValid(test2)}")  # Expected: True

# Test case 3: Invalid parentheses - mismatched
test3 = "(]"
print(f"Test 3: '{test3}' -> {isValid(test3)}")  # Expected: False
