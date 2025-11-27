def lengthOfLongestSubstring(s):
    sett = set()
    l, r = 0, 0
    max_len = 0
    n = len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
        sett.add(s[r])
        max_len = max(max_len, r-l+1)

    return max_len

s = "abcabcbb"
print(lengthOfLongestSubstring(s))
s = "bbbb"
print(lengthOfLongestSubstring(s))