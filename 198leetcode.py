class Solution:
    def __init__(self):
        print "init"
        self.res = None

    def solve(self,family,idx):
        if idx<0:
            return 0
        if self.res[idx]>=0:
            print ">=0",idx
            self.res[idx]
        else:
            self.res[idx] = max(self.solve(family,idx-1),family[idx]+self.solve(family,idx-2))
        return self.res[idx]

    def rob(self,family):
        print "rob"
        self.res = [-1]*len(family)
        return self.solve(family,len(family)-1)


s = Solution()
arr = [2,7,9,3,1]
print s.rob(arr)

