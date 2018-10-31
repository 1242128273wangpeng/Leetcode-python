class Solution:
    def __init__(self):
        self.lo = -1
        self.maxlen = -1
        print "5 leetcode second way"

    def solve(self,mstr):
        if len(mstr)<2:
            return 

        for i in range(len(mstr)-1):
            self.extendPalindrome(mstr,i,i)
            self.extendPalindrome(mstr,i,i+1)
        return mstr[self.lo:self.lo+self.maxlen]
    
    def extendPalindrome(self,mstr,j,k):
        print "extendPalindrome"
        while (j>=0 and k< len(mstr)-1 ) and (mstr[j] == mstr[k]):
            j-=1
            k+=1

        if self.maxlen < k-j-1:
            self.lo = j+1
            self.maxlen = k-j-1

s = Solution()
print s.solve("bbvvnnvvbb")


