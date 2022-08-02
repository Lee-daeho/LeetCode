###69. Sqrt(x) 22/08/02 ###

###My Solution -> Easy binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            mid = (l + r) // 2

            if mid ** 2 == x:
                return mid

            if mid ** 2 < x:
                l = mid + 1
            else:
                r = mid - 1

        return l - 1    #you just need right before

###faster solution

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1: return 1 #deal with exception
        l, r = 0, x
        while l <= r:
            mid = (r+l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid