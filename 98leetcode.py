class Solution(object):
    def __init__(self):
        print "98 leetcode solution"

    def solve(self,node):
            #self.helper(node,None,None)
        self.valid(node,None,None)
  
    def helper(self,node,minval,maxval):
        if node is None or node.val is None:
            return True
        if (minval is not None and node.val<=minval) or (maxval is not None and node.val>=maxval):
            return False
        return self.helper(node.left,minval,node.val) and self.helper(node.right,node.val,maxval)
    
    def valid(self, root, min_, max_):
        if root == None or root.val == None:
            return True
       
        if (min_ is not None and root.val <=min_) or (max_ is not None and root.val >= max_):
            return False
       
        return self.valid(root.left, min,root.val) and self.valid(root.right, root.val, max)

class Node(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


s = Solution()
n = Node(2)
l = Node(1)
r = Node(3)
n.left = l
n.right = r

#print "res is :",s.solve(n)
print "res is :",s.solve(n)
