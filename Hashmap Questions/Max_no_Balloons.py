'''
Name: Muhammad Ali Mosin Hasan
Date: 14/6/25
Problem: 1189: Maximum Number of Balloons
'''
from collections import defaultdict
def maxNumberOfBalloons(text):
    '''
    Counts the maximum number of times the word "balloon" can be formed from the characters in the input text.

    Args:
        text (str): Input string containing characters.

    Returns:
        int: Maximum number of times "balloon" can be formed.
    '''
    counter = defaultdict(int)
    balloon = 'balloon'

    for c in text:
        if c in balloon:
            counter[c] += 1
    
    if any(c not in counter for c in balloon):
        return 0
    else:
        return min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n'])
    
# Example usage 

text = "nlaebolko"
count = maxNumberOfBalloons(text)
print("Maximum number of 'balloon' that can be formed: " + str(count))

text = "loonbalxballpoon"
count = maxNumberOfBalloons(text)
print("Maximum number of 'balloon' that can be formed: " + str(count))

text = "leetcode"
count = maxNumberOfBalloons(text)
print("Maximum number of 'balloon' that can be formed: " + str(count))