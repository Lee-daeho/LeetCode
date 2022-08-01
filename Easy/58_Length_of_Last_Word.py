###58. Length of last word 22/08/01 ###

###My Solution

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        slist = s.split(' ')
        for i in range(len(slist)):
            if len(slist[-1 * (i + 1)]) != 0:
                return len(slist[-1 * (i + 1)])


### Funny one line solution ###
def lengthOfLastWord(self, s):
    return len(s.rstrip(' ').split(' ')[-1])


### official solution ###
class Solution:
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        while end > 0 and s[end] == " ": end -= 1
        beg = end
        while beg >= 0 and s[beg] != " ": beg -= 1
        return end - beg