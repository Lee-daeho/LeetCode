###28. Implement strStr() 22/07/31 ###

###my solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if not needle in haystack:
            return -1

        return haystack.find(needle)

### readable solution###
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

"aacabdkacaa"
###KMP solution -> the best ###
def strStr2(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    def kmp(str_):
        b, prefix = 0, [0]
        for i in range(1, len(str_)):
            while b > 0 and str_[i] != str_[b]:
                b = prefix[b - 1]
            if str_[b] == str_[i]:
                b += 1
            else:
                b = 0
            prefix.append(b)
        return prefix

    str_ = kmp(needle + '#' + haystack)
    n = len(needle)
    if n == 0:
        return n
    for i in range(n + 1, len(str_)):
        if str_[i] == n:
            return i - 2 * n
    return -1