class Solution:
    def isValid(self, s: str) -> bool:
        diction = {
           "(": ")",
           "[": "]",
           "{": "}" 
        }
        stack = []
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            elif(len(stack) == 0 or i != diction[stack.pop()]):
                return False
        return len(stack) == 0
        

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("[({}])"))
