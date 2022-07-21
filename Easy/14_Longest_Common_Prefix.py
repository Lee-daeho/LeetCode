###Longest Common Prefix 22/7/22###

###my solution
def longestCommonPrefix(strs: list[str]) -> str:

    rows = sorted(range(len(strs)), key=lambda i: len(strs[i]))

    for i in range(len(strs[rows[0]])):
        ref = strs[rows[0]][:len(strs[rows[0]])-i]
        ret = True
        for j in range(len(strs)):
            if j == rows[0]:
                continue

            if not ref == strs[j][:len(strs[rows[0]])-i]:
                ret = False

        if ret:
            return ref

    return ""


###short python solution
def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest

###great solution
def longestCommonPrefix(m):
    if not m: return ''
            #since list of string will be sorted and retrieved min max by alphebetic order
    s1 = min(m)
    s2 = max(m)

    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i] #stop until hit the split index
    return s1