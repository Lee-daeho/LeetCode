###27. Remove Element 22/07/31###

###my solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        while True:
            try:
                nums.remove(val)

            except:
                return len(nums)


###pointer based solution
def removeElement(self, nums, val):
start, end = 0, len(nums) - 1
while start <= end:
    if nums[start] == val:
        nums[start], nums[end], end = nums[end], nums[start], end - 1
    else:
        start +=1
return start