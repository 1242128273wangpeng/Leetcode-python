class Solution:
    def __init__(self):
        print("5 solution")

    def solve(self,mstr):
        print(mstr)
        resmax = -1
        res = ""
        dp = [[0]*10 for i in range(10)]
        for i in range(len(mstr)):
            for j in range(i+1):
                print(i,mstr[i],j,mstr[j])
                dp[j][i] = mstr[i]==mstr[j] and (i-j<=2 or mstr[j+1]==mstr[i-1])
                if dp[j][i]:
                    if i-j+1>resmax:
                        resmax = i-j+1
                        res = mstr[j:i+1]
        return res

s = Solution()
print(s.solve("bbvvbb"))
#print s.solve("abdcecdba")

