class Solution:
    def __init__(self,arr):
        self.arr = arr
        self.dp = [0]*len(arr)
        print "init 53_2"

    def solve(self):
        print "solve",self.arr,len(self.arr)
        for i,v in enumerate(self.dp):
            print i,v
            self.dp[i] = max([self.dp[i],self.dp[i-1]+self.arr[i]])
        return self.dp[len(self.dp)-1]
    
    def show(self):
        for i in self.dp:
            print i
            
s = Solution([-10,1,2,3,7,4,-5,-23,3,7,-21])
print s.solve()
s.show()

