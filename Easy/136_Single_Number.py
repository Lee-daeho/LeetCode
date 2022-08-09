###136. Single Number 22/08/09 ###

# My Solution after cheating -> Xor is so great wonderful fantastic solution!

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        return xor