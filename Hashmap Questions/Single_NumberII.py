from collections import Counter
def Single_NumberII(nums):
    count = Counter(nums)
    for key, freq in count.items():
        if freq != 3:
            return key
    return None

nums = [0, 1, 0, 1, 0, 1, 99]
result = Single_NumberII(nums)
print("The element which appeared once is: ", result)
