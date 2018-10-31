class Solution:
    def __init__(self):
        self.list = [-1, 0, 1, 2, -1, -4]
        print "15leetcode solution"


    def solve(self):
        res = list()
        nums_len = len(self.list)
        if nums_len<3:
            return res
        l,r,dif = 0,0,0
        self.list.sort()
        for i in range(nums_len-2):
            if self.list[i]>0:
                break
            if i>0 and self.list[i-1]==self.list[i]:
                continue
            l = i+1
            r = nums_len-1
            dif = -self.list[i]
            while l<r:
                if self.list[l]+self.list[r] == dif:
                    res.append([self.list[l],self.list[r],self.list[i]])
                    while l<r and self.list[l] == self.list[l+1]:
                        l +=1
                    while l<r and self.list[r] == self.list[r-1]:
                        r -=1
                    l +=1
                    r -=1
                elif self.list[l]+self.list[r] < dif:
                    l +=1
                else:
                    r -=1
        return res


s = Solution()
r = s.solve()
for i in r:
    print i

