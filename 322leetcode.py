import sys
class Solution:
    def __init__(self):
        print "init"

    def resolve(self,coins,amount):
        print "resolve"
        return self.search(0,coins,amount)

    def search(self,index,coins,amount):
        if amount<0:
            return sys.maxint
        if amount==0:
            return 0
        if index>=len(coins):
            return sys.maxint
        a = self.search(index,coins,amount-coins[index])
        b = self.search(index+1,coins,amount)
        print "a:",a,"b:",b
        return min(a+1,b)
    
s = Solution()
coins = [1, 2, 5]
amount = 11
print s.resolve(coins,amount)

