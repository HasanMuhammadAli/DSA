import time
def isHappy(n):
    def next(num):
        summ = 0
        while num > 0:
            digit = num % 10
            summ += digit ** 2
            num = num // 10
        return summ
    
    slow = n
    fast = n
    while fast != 1:
        slow = next(slow)
        fast = next(next(fast))
        
        if fast == 1:
            return True
        
        if slow == fast:
            return False
        
    return True    
        
print(isHappy(10))
            