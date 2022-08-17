### 338. Counting Bits 22/08/17###

###My Solution
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(n + 1):
            val = i
            while val != 0:
                if val % 2 == 1:
                    ans[i] += 1

                val = val // 2

        return ans

###DP solution  why DP problems always need to find pattern?
def countBits(self, n: int) -> List[int]:
    for i in range(num):
        counter[i] = counter[i // 2] + i % 2