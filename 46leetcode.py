class Solution:
    def __init__(self):
        self.a = [1,2,3]
        self.res = []
        print "permation"

    def perm1(self,idx):
        if idx>=len(self.a):
            print self.a
            self.res.append(self.a)
            return 
        for i in range(idx,len(self.a)):
            self.a[i],self.a[idx] = self.a[idx],self.a[i]
            self.perm1(idx+1)
            self.a[i],self.a[idx] = self.a[idx],self.a[i]
    
    def perm2(self,temp):
        if len(temp) == len(self.a):
            print temp
            self.res.append(temp)
            return 
        print "start perm",temp
        for i in range(0,len(self.a)):
            if self.a[i] not in temp:
                print "not in i",self.a[i]
                print "append before",temp
                temp.append(self.a[i])
                print "append after",temp
                self.perm2(temp)
                print "remove before",temp
                temp.remove(self.a[i])
                print "remove after",temp
            else:
                print "in i ",self.a[i]



if __name__ == "__main__":
    s = Solution()
    res = []
    s.perm2(res)

