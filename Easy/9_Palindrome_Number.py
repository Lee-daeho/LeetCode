###Palindrome Number 7/20###

#my solution
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    else:
        for i in range(len(str(x))):
            if i > (len(str(x)) - 1) // 2:
                return True
            else:
                if str(x)[i] == str(x)[-1 * (i + 1)]:
                    pass
                else:
                    return False

    return True

#best solutions
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False

    return str(x) == str(x)[::-1]

def isPalindrome(self, x: int) -> bool:
	if x<0:
		return False

	inputNum = x
	newNum = 0
	while x>0:
		newNum = newNum * 10 + x%10
		x = x//10
	return newNum == inputNum


def isPalindrome(self, x: int) -> bool:
    if x < 0 or (
            x > 0 and x % 10 == 0):  # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
        return False

    result = 0
    while x > result:
        result = result * 10 + x % 10
        x = x // 10

    return True if (x == result or x == result // 10) else False