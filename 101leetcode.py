class TreeNode:
    def __init__(self,x):
        self.val = x
        self.l = None
        self.r = None
class Solution:
    def helper(self,root):
        if root == None:
            return True
        return self.isSymmetric(root.l,root.r)
    def isSymmetric(self,q,p):
        if q==None and p==None:
            return True
        if q==None or p==None:
            return False
        if q.val == p.val:
            return self.isSymmetric(q.l,p.r) and self.isSymmetric(q.r,p.l)
        else:
            return False

if __name__ == "__main__":
    b = TreeNode(3)
    b.l = TreeNode(4)
    b.r = TreeNode(6)
    c = TreeNode(3)
    c.l = TreeNode(6)
    c.r = TreeNode(4)
    a = TreeNode(1)
    a.l = b
    a.r = c
    s = Solution()
    print s.helper(a)

