### 858. Mirror Reflection 22/08/04###


###My solution after cheating -> this problem looks like a geometry problem
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0: p, q = p // 2, q // 2

        return 1 - p % 2 + q % 2