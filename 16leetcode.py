class Solution:
    def __init__(self):
        self.list=[-1,2,1,4]
        self.res=list()
        print("solution 16leetcode")

    def solve(self,target):
        if self.list is None or len(self.list)==0:
            return self.list
        self.res = -1
        m = abs(self.res-target)
        self.list.sort()
        for i in range(len(self.list)-2):
            if i>0 and self.list[i-1]==self.list[i]:
                continue
            l = i+1;
            r = len(self.list)-1
            while l<r:
                temp = self.list[l]+self.list[r]+self.list[i];
                if m>abs(temp-target):
                    m = abs(temp-target)
                    self.res = temp
                if temp>target:
                    r-=1
                    while l<r-1 and self.list[r]==self.list[r-1]: r-=1
                elif temp<target:
                    l+=1
                    while l<r-1 and slef.list[l]==self.list[l+1]: l+=1
        print("target:",target,"res:",self.res)
        return self.res
s = Solution()
s.solve(1)
