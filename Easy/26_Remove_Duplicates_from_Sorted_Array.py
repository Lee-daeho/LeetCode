###26. Remove Dulicates for Sorted Array 22/07/29###

###My solution ###
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))

        return len(nums)

###Im not sure that why nums = sorted(list(set(nums))) works really well on my pycharm and terminal!!! and does not in leetcode