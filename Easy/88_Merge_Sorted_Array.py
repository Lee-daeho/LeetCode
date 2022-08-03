###88. Merge Sorted Array 22/08/03###

###My Solution for O(m+n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            nums1[:] = nums2[:]

        elif n == 0:
            pass

        else:
            piv = m + n - 1

            while m > 0 and n > 0:
                if nums1[m - 1] > nums2[n - 1]:
                    nums1[piv] = nums1[m - 1]
                    m = m - 1
                else:
                    nums1[piv] = nums2[n - 1]
                    n = n - 1
                piv = piv - 1

            if n > 0:
                nums1[:n] = nums2[:n]

###shorter sorlution
def merge(self, nums1, m, nums2, n):
    while n > 0:
        if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1