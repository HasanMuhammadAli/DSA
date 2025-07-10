'''
Name: Muhammad Ali Mosin Hasan
Date: 10/7/25
Problem: 1768:  Merge Strings Alternately
'''

def mergeAlternatingly(word1, word2):
    result = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
        
    # Append the remainder of the longer word
    result.append(word1[i:])
    result.append(word2[j:])
    return ''.join(result)


word1 = "abc"
word2 = "pqr"
print(mergeAlternatingly(word1, word2))