def findTheDifference(s, t):
    freq_s = {}
    freq_t = {}

    for ch in s:
        freq_s[ch] = freq_s.get(ch, 0)+1
    
    for ch in t:
        freq_t[ch] = freq_t.get(ch, 0)+1

    
    for ch in t:
        if freq_t[ch] != freq_s.get(ch, 0):
            return ch
        
    return None

s = "abcd"
t = "abcde"
print(findTheDifference(s, t))