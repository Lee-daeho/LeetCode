### Pascal's Triangle II 22/08/11###


###My Solution after cheating --> The problem says "Could you optimize your algorithm to use only O(rowIndex) extra space?"
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [1]

        for _ in range(rowIndex):
            output = [x + y for x, y in zip(output + [0], [0] + output)]

        return output

### Another solution
class Solution():

    def getRow(self, r):
        ans = [1] * (r + 1);
        up = r
        down = 1
        for i in range(1, r):
            ans[i] = int(ans[i - 1] * up / down)
            up = up - 1
            down = down + 1

        return ans