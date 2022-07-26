###20. Valid Parentheses 22/07/26 ###

###My Solution after cheating on solutions###
def isValid(s: str) -> bool:
    dt = {'[': ']', '{': '}', '(': ')'}
    stack = []
    if len(s) % 2 == 1 or s[0] in ['}', ')', ']'] or s[-1] in ['[', '(', '{']:
        return False

    else:
        for c in s:
            if c in dt.keys():
                stack.append(c)
            else:
                if stack == [] or not dt[stack.pop()] == c:
                    return False
                else:
                    pass

        return True if stack == [] else False


###reference solution###

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


###pop error catch trick###
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = ['N']
    m = {')': '(', ']': '[', '}': '{'}
    for i in s:
        if i in m.keys():
            if stack.pop() != m[i]:
                return False
        else:
            stack.append(i)

    return len(stack) == 1