'''
Name: Muhammad Ali Mosin Hasan
Date: 26/7/25
Problem: 274: H-Index
'''

def h_index(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i >= c:
            return i
    return len(citations)

# Example usage
print(h_index([3, 0, 6, 1, 5]))
print(h_index([1, 3, 1]))