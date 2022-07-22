### Two Sum ###

###my damn stupid solution
def twoSum(nums: list[int], target: int) -> list[int]:
    dt = {}
    for i in range(len(nums)):
        if abs(2 * nums[i] - target) not in dt:
            dt[abs(2 * nums[i] - target)] = i

        else:
            if nums[dt[abs(2 * nums[i] - target)]] + nums[i] == target:
                return [dt[abs(2 * nums[i] - target)], i]


### python solution
def twoSum(self, nums: list[int], target: int) -> list[int]:

    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]