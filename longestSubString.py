class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        res = 0
        length = len(s)
        dictionary = {}
        i = 0
        
        for j in range(length):
            if(s[j] in dictionary):
                i = max(i, dictionary[s[j]]+1) 

            dictionary[s[j]] = j
            res = max(res,j-i+1)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcdeafbdgcbb"))