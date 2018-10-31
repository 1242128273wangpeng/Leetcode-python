class Solution(object):
    def __init__(self):
        print "94 leetcode solution"

    def solve(self,cur):
        if cur is None:
            return 
        else:
            self.solve(cur.left)
            print "node:",cur.val
            self.solve(cur.right)

class Node(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

s = Solution()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.right = n2
n2.left = n3
s.solve(n1)
