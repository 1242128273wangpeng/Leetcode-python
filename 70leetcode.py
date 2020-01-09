class Solution:
    def climbStairs(self,n):
        if n in range(1,2):
            return n
        else:
            a = [0]*n
            a[0] = 1
            a[1] = 2
            for i in range(2,n):
                a[i] = a[i-1]+a[i-2]
            return a[n-1]



s = Solution()
print(s.climbStairs(8))
print(s.climbStairs(3))


