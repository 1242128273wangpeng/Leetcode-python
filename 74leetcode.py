class Solution:
    def __init__(self):
        print("74 leetcode")

    def solve(self,target):
        a = [[0 for i in range(5)] for j in range(5)]
        a[0] = [2,4,5,7,11]
        a[1] = [3,6,7,8,13]
        a[2] = [5,7,8,9,14]
        a[3] = [8,12,15,17,19]
        a[4] = [9,16,18,21,25]
        print(a)
        if len(a)==0:
            return
        i = 0
        j = len(a[0])-1
        while i<len(a) or j>=0:
            temp = a[i][j]
            if target>temp:
                i+=1
            elif target<temp:
                j-=1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.solve(15))

