import sys
class Solution:
    def __init__(self):
        print("init")

    def solve(self,price):
        if len(price)<=1:
            return 0
        s0 = 0
        s1 = -price[0]
        s2 = -sys.maxsize
        for i in range(1,len(price)):
            pre0 = s0
            pre1 = s1
            pre2 = s2
            s0 = max(pre0,pre2)
            s1 = max(pre0-i,pre1)
            s2 = pre1+i
        return max(s0,s2)

s = Solution()
p = [1,2,3,0,3]
print(s.solve(p))
