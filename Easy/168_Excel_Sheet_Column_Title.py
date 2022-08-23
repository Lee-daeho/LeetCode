### 168. Excel Sheet Column Title 22/08/23###

###My Solution
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""

        A = ord('A')

        while columnNumber > 0:
            columnNumber -= 1

            s = chr(A + columnNumber % 26) + s

            columnNumber = columnNumber // 26

        return s