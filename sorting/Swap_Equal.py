def areAlmostEqual(s1, s2):
    if s1 == s2:
        return True
    idx = []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        elif s1[i] != s2[i]:
            idx.append(i)
    
    if len(idx) != 2:
        return False

    i, j = idx
    s1 = list(s1)
    s1[i], s1[j] = s1[j], s1[i]
    if "".join(s1) == s2:
        return True
    return False

