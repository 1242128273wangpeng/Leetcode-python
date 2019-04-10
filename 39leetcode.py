import copy
class Solution:
    def __init__(self):
        print "leetcode 39"
    
    def combinationSum(self):
        a = [3,2,4,7]
        path = list()
        res = list()
        self.solve(a,res,0,path,7)
        return res

    def solve(self,arr,res,start,path,target):
        print "target",target
        if len(arr)==0:
            return 
        if target<0:
            return 
        if 0==target:
            # 1
            #res.append(copy.copy(path))
            # 2
            res.append(path)
            return
        #1
        #for i in range(start,len(arr)):
        #    print "i",i
        #    path.append(arr[i])
        #    self.solve(arr,res,i,path,target-arr[i])
        #    path.pop()
        #2
        for i in range(start,len(arr)):
            self.solve(arr,res,i,path+[arr[i]],target-arr[i])
            print "i",i," path",path
        
if __name__ == "__main__":
    s = Solution()
    print s.combinationSum()



        
