import sys
class Solution:
    def __init__(self):
        print "init"

    def solve(self,coins,amount):
        print "solve"
        return self.search(coins,amount)

    def search(self,coins,amount):
        print "search"
        if amount == 0:
            return 0
        dp = (amount+1)*[sys.maxint]
        dp[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if i>=j and dp[i-j]<>sys.maxint:
                    dp[i] = min(dp[i-j]+1,dp[i])
        
        if dp[amount] >0 and dp[amount]<sys.maxint:
            return dp[amount]
        else:
            return -1

s = Solution()
coins = [1, 2, 5]
amount = 11
print s.solve(coins,amount)
