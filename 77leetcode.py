import copy
class Solution:
    def __init__(self):
        print "leetcode77"

    def combine(self,n,k):
        res = list()
        path = list()
        self.solve(1,n,k,res,path)
        return res
    def solve(self,start,n,k,res,path):
        if k==0:
            res.append(copy.copy(path))
            print "path:",path,"res:",res
            return 
        for i in range(start,n+1):
            path.append(i)
            self.solve(i+1,n,k-1,res,path)
            p = path.pop()
            print p
            

if __name__ == "__main__":
    s = Solution()
    print s.combine(4,2)

