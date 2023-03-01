class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        previous = 0
        romans = {"I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
        for i in s:
            if(previous < romans[i]):
                res += romans[i] - previous*2
            else:
                res += romans[i]
            previous = romans[i]
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))