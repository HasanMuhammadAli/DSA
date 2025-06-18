'''
Name: Muhammad Ali Mosin Hasan
Date: 18/6/25
Problem: 49: Group Anagrams
'''
from collections import defaultdict
def groupAnagrams(strs):
    '''
    Groups anagrams from a list of strings.

    Args:
        strs (List[str]): List of strings to be grouped.

    Returns:
        List[List[str]]: List of lists, where each sublist contains anagrams.
    '''
    anagrams_dict = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        anagrams_dict[key].append(s)
    return anagrams_dict.values()

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = groupAnagrams(strs)
print("Grouped Anagrams:")
for group in anagrams:
    print(group)

# Example usage with different input
strs = [""]
anagrams = groupAnagrams(strs)
print("Grouped Anagrams:")
for group in anagrams:
    print(group)