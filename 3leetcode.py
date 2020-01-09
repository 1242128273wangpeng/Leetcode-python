class Solution:
    def __init__(self):
        self.mstr = "abcbcbb"
        print("3 leetcode solution")


    def solve(self):
        allmap = dict()
        j = 0
        res = -1
        for i in range(len(self.mstr)):
            if self.mstr[i] in allmap:
                j=allmap[self.mstr[i]]+1
            res = max(res,i-j+1) 
            allmap[self.mstr[i]] = i
        return res

    def solve2(self):
        allset = set()
        j = 0
        res = -1
        for i in range(len(self.mstr)):
            if self.mstr[i] in allset:
                allset.remove(self.mstr[i])
            else:
                allset.add(self.mstr[i])
                res = max(res,len(allset))
        return res

    

s = Solution()
print(s.solve())
        
