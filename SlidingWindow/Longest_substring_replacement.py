def characterReplacement(s, k):
    freq = {}
    left = 0
    max_len = 0
    max_freq = 0  # max frequency of any char in the current window

    for right in range(len(s)):
        # add current char to freq
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])

        # check if window is valid
        if (right - left + 1) - max_freq > k:
            # shrink window
            freq[s[left]] -= 1
            left += 1

        # update max length
        max_len = max(max_len, right - left + 1)

    return max_len

s = "ABAB"
k = 2
print(characterReplacement(s, k))