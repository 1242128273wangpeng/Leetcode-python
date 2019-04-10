class Solution:
    def __init__(self):
        print ""

    def solve(self,arr):
        if len(arr)==0 or len(arr[0])==0:
            return
        res = 0
        n = len(arr)
        m = len(arr[0])
        print n,m
        for i in range(n):
            for j in range(m):
                if arr[i][j]==1:
                    print i,j
                    #self.dfs(arr,i,j)
                    self.bfs(arr,i,j)
                    res+=1
        return res

    def dfs(self,arr,x,y):
        dx =(-1,0,1,0) 
        dy =(0,-1,0,1)
        arr[x][y] = 0
        for i in range(4):
            newx = dx[i]+x
            newy = dy[i]+y
            if newx>=0 and newx<len(arr) and newy>=0 and newy<len(arr[0]) and arr[newx][newy]==1:
                self.dfs(arr,newx,newy)
    
    def bfs(self,arr,x,y):
        res = list()
        res.append((x,y))
        dx = (-1,0,1,0)
        dy = (0,1,0,-1)
        while res:
            x,y = res.pop(0)
            for i in range(4):
                newx = x+dx[i]
                newy = y+dy[i]
                if newx>=0 and newx<len(arr) and newy>=0 and newy<len(arr[0]) and arr[newx][newy]==1:
                    arr[newx][newy] = 0
                    res.append((newx,newy))
            

if __name__ == "__main__":
    s = Solution()
    a = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
    print s.solve(a)



