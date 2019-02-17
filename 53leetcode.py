class Solution:
    def __init__(self):
        self.list = [-2,1,-3,4,-1,2,1,-5,4]
        print "53 leetcode"

    def solve(self):
        resmax = -1
        res = -1
        for i in self.list:
            if resmax<0:
                resmax = 0
            resmax = resmax + i
            res = max(res,resmax)
        return res

s= Solution()
print s.solve()

