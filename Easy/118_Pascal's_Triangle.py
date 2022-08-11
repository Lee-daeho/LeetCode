### 118. Pascal's Triangle 22/08/11###

###My Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pascal = [[1]]

        for i in range(2, numRows + 1):

            new_line = [1] * i

            if i > 2:
                for j in range(1, i - 1):
                    new_line[j] = pascal[i - 2][j - 1] + pascal[i - 2][j]

            pascal.append(new_line)

        return pascal


###Best Solution
def generate(self, numRows):
    res = [[1]]
    for i in range(1, numRows):
        res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
    return res[:numRows]