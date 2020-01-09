class Solution:
    def __init__(self,m,n):
        self.m = m
        self.n = n
        self.arr = [[0]*m for _ in range(n)]
        print("62 leetcode",self.arr)

    def solve(self,m,n):
        print("solve")
        for i in range(m):
            self.arr[0][i] = 1

        for j in range(n):
            self.arr[j][0] = 1
        print("after",self.arr)
        for k in range(1,m):
            for l in range(1,n):
                self.arr[l][k] = self.arr[l][k-1]+self.arr[l-1][k]
        print("last",self.arr)

    def solve2(self):
        for i in range(self.n):
            for j in range(self.m):
                if i==0 or j==0:
                    self.arr[i][j] = 1
                else:
                    self.arr[i][j] = self.arr[i-1][j] + self.arr[i][j-1]
        print("solve2",self.arr)
if __name__ == "__main__":
    s = Solution(7,3)
    #s.solve(7,3)
    s.solve2()
