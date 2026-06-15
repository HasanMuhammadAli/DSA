import heapq
# Binary Tree
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
print("Binary Tree: ", A)
# BT to Heap(Min Heap)
heapq.heapify(A)
print("Heap: ",A)


# Heap push T:O(log N)
heapq.heappush(A, 4) # this add 4 to heap A
print("Heap after insertion of 4: ",A)


# Heap pop T:O(log N)
minn = heapq.heappop(A) # removes the minimum from the heap as the root of the heap is minimum
print("Heap after poping:", A)


# Heap Sort T:O(N log N) S:O(N)
# O(1) space is possible via swapping, but it is complex
def heapSort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    
    return new_list

nums = [7, 2, 9, 1, 5]
print("Before Sorting: ", nums)
print("Heap Sort Output: ", heapSort(nums))


# Heap Push Pop T:O(log N)
print("Before heap push pop opertion: ", A)
heapq.heappushpop(A, 99) # removes min and adds 99
print("After heap push pop operation: ", A)


# Max Heap [Not supported directly by library]
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
print("B before heapify: ", B)
n = len(B)
# negate all value
for i in range(n):
    B[i] = -B[i]
print("B after negate but before heapify: ", B)
heapq.heapify(B)
print("B after heapify: ", B)
largest = -heapq.heappop(B) #12 # we re-negate to get original value
print("Getting largets value through max heap: ", largest)
print("B before inserting: ", B)
heapq.heappush(B, -7) # inserts 7 not -7
print("B after insertion: ", B)


# Peak at min T:O(1)
print("Peak of min: ", A[0])


# Build heap from scratch
C = [-5, 4, 2, 1, 7, 0, 3]
heap = []
for x in C:
    heapq.heappush(heap, x)
print("C: ", heap)


# Putting tuples of items on the heap
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]
from collections import Counter
counter = Counter(D)
heap = []
for k, v in counter.items():
    heapq.heappush(heap, (v, k))

print("Heap containing tuple: ", heap)
# Heap element example : (2, 3) 2 is freq and 3 is key

