class Solution:
    def __init__(self):
        self.list = ["flow","flower","fly"]
        print("leetcode 14 solution")

    def find(self):
        minlen = len(self.list[0])
        for i in self.list:
            minlen<len(i)
            minlen = len(i)

        for k in range(0,minlen):
            for j in self.list:
                if self.list[0][k]!=j[k]:
                    return j[0:k]

        
            

s = Solution()
print(s.find())
