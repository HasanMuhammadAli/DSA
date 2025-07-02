'''
Name: Muhammad Ali Mosin Hasan
Date: 2/7/25
Problem: 155: Min Stack
'''


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else: 
            self.min_stack.append(val)

    def pop(self) -> None:  
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

#Example use cases
#example one
print("Example1:")
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Returns -3
minStack.pop()
print(minStack.top())     # Returns 0
print(minStack.getMin())  # Returns -2

#example two
print("Example2:")
minStack = MinStack()
minStack.push(5)
minStack.push(3)
minStack.push(7)
minStack.push(1)
print(minStack.getMin())  # Returns 1
minStack.pop()
print(minStack.getMin())  # Returns 3
print(minStack.top())     # Returns 7