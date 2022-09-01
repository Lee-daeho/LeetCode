### 15. 3Sum 22/09/01

###My Solution after cheating
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = length - 1

            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                if sum < 0:
                    l += 1

                elif sum > 0:
                    r -= 1

                else:
                    res.append([nums[l], nums[i], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

