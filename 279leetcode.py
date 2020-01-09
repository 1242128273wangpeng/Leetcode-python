class Solution:
    def __init__(self):
        print("279leetcode")

    def solve(self,n):
        print("solve")
        dp = [-1 for i in range(0,n+1)]
        print(len(dp),dp)
        dp[0] = 0
        res = list()
        res.append(0)
        while res:
            temp = res.pop(0)
            print("temp",temp)
            if temp==n:
                return dp[temp]
            for i in range(1,n):
                if i*i+temp<=n and dp[i*i+temp]==-1:
                        dp[i*i+temp] = dp[temp]+1
                        res.append(i*i+temp)
        return dp[n]


                    

if __name__ == "__main__":
    s = Solution()
    a = 13
    b = 12
    print(s.solve(a))

