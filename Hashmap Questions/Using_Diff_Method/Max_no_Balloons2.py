'''
Name: Muhammad Ali Mosin Hasan
Date: 4/8/25
Problem: 1189: Maximum Number of Balloons
'''
from collections import defaultdict
from collections import Counter
def maxNumberOfBalloons(text):
    '''
    Counts the maximum number of times the word "balloon" can be formed from the characters in the input text.
    '''
    '''
    # Using defaultdict to count characters in the text
    counter = defaultdict(int)
    balloon = 'balloon'

    for c in text:
        if c in balloon:
            counter[c] += 1
    
    if any(c not in counter for c in balloon):
        return 0
    else:
        return min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n'])
    '''

    # Using Counter to count characters in the text
    counter = Counter(text)
    balloon = 'balloon'

    if any(c not in counter for c in balloon):
        return 0

    # Calculate the maximum number of times "balloon" can be formed
    return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])


# Example usage 
text = "nlaebolko"
count = maxNumberOfBalloons(text)
print("Maximum number of 'balloon' that can be formed: " + str(count))# Output: 1

text = "loonbalxballoon"
count = maxNumberOfBalloons(text)
print("Maximum number of 'balloon' that can be formed: " + str(count))# Output: 2

text = "loonbalxballpoon"
count = maxNumberOfBalloons(text)
print("Maximum number of 'balloon' that can be formed: " + str(count))# Output: 2

text = "leetcode"
count = maxNumberOfBalloons(text)
print("Maximum number of 'balloon' that can be formed: " + str(count))# Output: 0