### 125. Valid Palindrome 22/08/15###

###My Solution -> wtf

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1

            elif not s[r].isalnum():
                r -= 1

            else:
                if s[l].lower() != s[r].lower():
                    return False

                else:
                    l += 1
                    r -= 1

        return True


### Cool looking solution
class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]