### 67. Add Binary 22/08/02 ###

###My Solution

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        inta = int(0)
        intb = int(0)

        for i in range(len(a)):
            inta += 2 ** (i) * int(a[~i])

        for i in range(len(b)):
            intb += 2 ** (i) * int(b[~i])

        return format(inta + intb, 'b')

###super hot solution

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), 'b')


###the most understandable solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]