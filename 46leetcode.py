import copy
class Solution:
    def __init__(self):
        self.a = [1,2,3]
        self.res = []
        print "permation"

    def perm1(self,idx):
        if idx>=len(self.a):
            self.res.append(copy.copy(self.a))
            return 
        for i in range(idx,len(self.a)):
            self.a[i],self.a[idx] = self.a[idx],self.a[i]
            self.perm1(idx+1)
            self.a[i],self.a[idx] = self.a[idx],self.a[i]
        return self.res   
   
    def perm2(self,temp):
        if len(temp) == len(self.a):
            self.res.append(copy.copy(temp))
            return 
        for i in range(0,len(self.a)):
            if self.a[i] not in temp:
                temp.append(self.a[i])
                self.perm2(temp)
                temp.remove(self.a[i])

        return self.res

if __name__ == "__main__":
    s = Solution()
    res = []
    #print s.perm2(res)
    print s.perm1(0)

