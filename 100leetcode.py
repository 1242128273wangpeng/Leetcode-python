class TreeNode:
    def __init__(self,x):
        self.val = x
        self.l = None
        self.r = None

class Solution:
    def sameTree(self,p,q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if q.val == p.val:
            return self.sameTree(q.l,p.l) and self.sameTree(q.r,p.r) 
        else:
            return False

if __name__ == "__main__":
    a = TreeNode(1)
    a.l = TreeNode(2)
    a.r = TreeNode(3)
    b = TreeNode(1)
    b.l = TreeNode(9)
    b.r = TreeNode(3)
    s = Solution()
    print s.sameTree(a,b)
