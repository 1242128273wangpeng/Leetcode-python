class Solution:
    def __init__(self):
        self.res = list()
        self.list = [2,7,11,15]
        print "1leetcode Solution"

    def solve(self,target):
        l = 0
        r = len(self.list)-1
        while l<r:
            if self.list[l]+self.list[r] == target:
                self.res.append(l)
                self.res.append(r)
                return self.res
            elif self.list[l]+self.list[r]>target:
                r-=1
            else:
                l+=1

    def solve2(self,target):
        allmap = dict()
        for i in range(len(self.list)):
            if allmap.has_key(target-self.list[i]):
                lastvalue = allmap[target-self.list[i]]
                self.res.append(lastvalue)
                self.res.append(i)
                return self.res
            else:
                allmap[self.list[i]] = i


s = Solution()
#print s.solve(13)
print s.solve2(13)
