###66. Plus One 22/08/01 ###

###My solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 0

        for i in range(len(digits)):
            digit += digits[i] * (10 ** (len(digits) - 1 - i))

        digit += 1

        return [int(i) for i in str(digit)]

###super hot solution
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)