class Solution:
   
    def dfs(self,digits,index,path,res,d):
        if index == len(digits):
            res.append("".join(path))
            return 
        digit= int(digits[index])
        print "digit:",digit
        for c in d.get(digit,[]):
            print c
            path.append(c)
            self.dfs(digits,index+1,path,res,d)
            print path
            path.pop()

    def leeterCombine(self,digits):
        if len(digits) == 0:
            return []
        d = {1:"",2:"abc",3:"def",4:"ghi",5:"jkl"}
        res = []
        self.dfs(digits,0,[],res,d)
        return res
 
solution = Solution()
print solution.leeterCombine("23")
print type(solution),Solution
