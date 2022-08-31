### 11. Container With Most Water 22/08/31###

###My Solution - Perfect!
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxarea = 0

        while l < r:
            if height[l] > height[r]:
                area = (r - l) * height[r]
                r -= 1

            else:
                area = (r - l) * height[l]
                l += 1

            if area > maxarea:
                maxarea = area

        return maxarea


