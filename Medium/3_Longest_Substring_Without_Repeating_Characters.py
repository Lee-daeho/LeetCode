### 3. Longest Substring Without Repeating Characters 22/08/16 ###

###My Solution  : Please try to think it more. I almost could solve it by myself. Think more
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        start = 0
        seen = {}

        for i, char in enumerate(s):
            if char in seen.keys() and start <= seen[char]:
                start = seen[char] + 1

            else:
                length = max(length, i - start + 1)

            seen[char] = i

        return length