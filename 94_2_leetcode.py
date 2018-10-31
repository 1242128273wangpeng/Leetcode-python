class Solution(object):
    def __init__(self):
        self.res = list()
        self.stack = list()
        print "94 leetcode solution"

    def solve(self,cur):
        if cur is None:
            return 
        else:
            while True:
                if cur is not None:
                    self.stack.append(cur)
                    cur = cur.left
                else:
                    if len(self.stack)==0:
                        return self.res
                    node = self.stack.pop()
                    self.res.append(node.val)
                    cur = node.right
            return self.res



class Node(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None




n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.right =n2
n2.left =n3

s = Solution()
print s.solve(n1)
