class Solution:
    def buy(self,prices):
        print("buy")
        if len(prices)<2:
            return 0
        imin = prices[0]
        bene = 0
        for i,v in enumerate(prices):
            if v<imin:
                imin = v
            else:
                if (v-imin)>bene:
                    bene = v-imin
        return bene
s = Solution()
t = [7,1,5,3,6,4]
m = [7,6,4,3,1]
c = []
print(s.buy(t))


        

