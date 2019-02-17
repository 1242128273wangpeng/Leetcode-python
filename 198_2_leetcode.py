class Solution:
    def __init__(self):
        print "198_2_leetcode"
    def solve(self,family):
        a = 0
        b = 0
        for i in range(len(family)):
            a,b = b,max(a+family[i],b)
            print i,a,b
        print a,b
        

s = Solution()
family = [ 1, 3, 4, 5, 3, 2 ]
s.solve(family)
