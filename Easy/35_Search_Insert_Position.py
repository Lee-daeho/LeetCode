### 35. Search Insert Position 22/08/01 ###

###my solution of binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        if nums[l] == target:
            return l

        if nums[r] == target:
            return r

        if nums[(l + r) // 2] == target:
            return (l + r) // 2

        while l <= r:
            if nums[(l + r) // 2] == target:
                return (l + r) // 2

            elif nums[(l + r) // 2] > target:
                r = (l + r) // 2 - 1

            else:
                l = (l + r) // 2 + 1

        return r + 1    #can be just return l




