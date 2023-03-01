class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        neg = []
        pos = []
        zer = []
        nums.sort()
        res = set()
        for i in nums:
            if i > 0:
                pos.append(i)
            elif i < 0:
                neg.append(i)
            else:
                zer.append(i)
        N, P = set(neg), set(pos)
        if(len(zer) >= 3):
            res.add((0,0,0))
        if zer:
            for x in P:
                if -x in N:
                    res.add((-x,0,x))
        for x in range(len(neg)):
            for y in range(x+1, len(neg)):
                to_check = -(neg[x] + neg[y])
                if (to_check in P):
                    res.add((neg[x],neg[y],to_check))
        for x in range(len(pos)):
            for y in range(x+1, len(pos)):
                to_check = -(pos[x] + pos[y])
                if (to_check in N):
                    res.add((pos[x],pos[y],to_check))
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([1,1,-2]))
    print(s.threeSum([-1,0,1,0]))
    print(s.threeSum([-1,0,1,2,-1,-4]))
    print(s.threeSum([0,1,1]))
    print(s.threeSum([0,0,0]))