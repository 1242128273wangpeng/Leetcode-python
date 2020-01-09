class Solution:
    def __init__(self):
        print("leetcode 188")

    def solve(self,hsum):
        res = []
        for i in range(0,hsum):
            res.append([])
            for j in range(0,i+1):
                if j in (0,i):
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1]+res[i-1][j])
        print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    s.solve(6)
