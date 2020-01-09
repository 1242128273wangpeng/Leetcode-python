class TreeNode:
    def __init__(self,x):
        self.val = x
        self.l = None
        self.r = None

class Solution:
    def __init__(self):
        self.i = 0
    def helper(self,root,i):
        self.i = i
        print("leetcode104",self.i)
        if root==None:
            return
        return max(self.helper(root.l,i+1),self.helper(root.r,i+1))
  
    def helper2(self,root):
        if root == None:
            return 0
        return max(self.helper2(root.l),self.helper2(root.r))+1

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(8)
    h = TreeNode(9)
    a.l = b
    a.r = c
    b.l = d
    b.r = e
    c.l = f
    c.r = g
    d.l = h
    s = Solution()
    #s.helper(a,s.i)
    #print "helper",s.i
    print("helper2",s.helper2(a))
