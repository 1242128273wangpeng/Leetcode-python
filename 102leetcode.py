class TreeNode:
    def __init__(self,x):
        self.val = x
        self.l = None
        self.r = None

class Solution:
    def __init__(self):
        print "levelOrder"

    def levelOrder(self,root):
        if root == None:
            return 
        result = []
        result.append(root)
        while result:
            ret = []
            retlen = len(result)
            for i in range(retlen):
                tmp = result.pop(0)
                ret.append(tmp.val)
                if tmp<>None and tmp.l<>None:
                    ret.append(tmp.l)
                if tmp<>None and tmp.r<>None:
                    ret.append(tmp.r)
        result.append(ret)
        print result

if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    c.l = TreeNode(15)
    c.r = TreeNode(7)
    a.l = b
    a.r = c
    s = Solution()
    s.levelOrder(a)


