class Solution:
    def __init__(self):
        self.st =list()
        print("130leetcode")

    def solve(self,arr):
        n = len(arr)
        m = len(arr[0])
        self.st = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            if arr[i][0]=="O":
                self.bfs(arr,i,0)
            if arr[i][m-1] == "O":
                self.bfs(arr,i,m-1)
        for j in range(m):
            if arr[0][j]=="O":
                self.bfs(arr,0,j)
            if arr[n-1][j]=="O":
                self.bfs(arr,n-1,j)
        for a in range(n):
            for b in range(m):
                if arr[a][b]!="Y":
                    arr[a][b] = "X"
                else:
                    arr[a][b] = "O"

        return arr

    def dfs(self,arr,x,y):
        dx= (-1,0,1,0)
        dy= (0,-1,0,1)
        arr[x][y] = "Y"
        for i in range(4):
            newx=x+dx[i]
            newy=y+dy[i]
            if newx>=0 and newx<len(arr) and newy>=0 and newy<len(arr[0]):
                print(newx,newy)
                if arr[newx][newy]=="O":
                    self.dfs(arr,newx,newy)

    def bfs(self,arr,x,y):
        res = list()
        res.append((x,y))
        while res:
            a,b = res.pop(0)
            if arr[a][b]!="O":
                continue
            arr[a][b] = "Y"
            dx,dy = (-1,0,1,0),(0,-1,0,1)
            for i in range(4):
                nx,ny = a+dx[i],b+dy[i]
                if nx>=0 and nx<len(arr) and ny>=0 and ny<len(arr[0]):
                    res.append((nx,ny))


if __name__ == "__main__":
    s = Solution()
    arr =[["X","X","X","X"],["X","O","O","X"],["X","O","X","X"],["O","X","X","X"]]
    print(s.solve(arr))

