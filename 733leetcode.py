class Solution:
    def __init__(self):
        print("733leetcode")

    def solve(self,arr,x,y,newColor):
        if len(arr)==0 or len(arr[0])==0:
            return 
        print("solve")
        dx = [-1,0,1,0] 
        dy = [0,1,0,-1]
        oldColor = arr[x][y]
        if oldColor==newColor:
            return
        arr[x][y] = newColor
        for i in range(4):
            newx = x+dx[i]
            newy = y+dy[i]
            print(newx,newy)
            if newx>=0 and newx<len(arr) and newy>=0 and newy<len(arr[0]) and arr[newx][newy]==oldColor:
               self.solve(arr,newx,newy,newColor)
        return arr



if __name__ == "__main__":
    s = Solution()
    arr = [1,1,1],[1,1,0],[1,0,0]
    print(s.solve(arr,1,1,9))
