class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNum = 0
        aux = x 
        while (x > 0):
            lastDigit = x % 10
            revNum = (revNum*10) + lastDigit
            x = int(x / 10)
        if (revNum == aux):
            print("y")
        else:
            print("n")

if __name__ == "__main__":
    s = Solution()
    s.isPalindrome(121)