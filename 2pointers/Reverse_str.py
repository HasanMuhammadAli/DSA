def reverse_str(s):
    start = 0
    end = len(s)-1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    print(s)

reverse_str(["h","e","l","l","o"])
reverse_str(["h","e","l","l","o","a"])