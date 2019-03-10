class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        print "levelOrder"

    def levelOrder(self,root):
        if root == None:
            return 
        queue = [root]
        result = []
        print "root type",type(root)
        while queue:
            ret = []
            retlen = len(queue)
            for i in range(retlen):
                tmp = queue.pop(0)
                print type(tmp),retlen
                ret.append(tmp.val)
                if tmp<>None and tmp.l<>None:
                    print "append l"
                    queue.append(tmp.l)
                if tmp<>None and tmp.r<>None:
                    print "append r"
                    queue.append(tmp.r)
            result.append(ret)
        print result

    def levelOrder1(self,root):
        res = []
        queue = [root]
        while queue:
            len_queue = len(queue)
            l = list()
            for i in range(len_queue):
                print "i",i
                temp = queue.pop(0)
                l.append(temp.val)
                print "temp.val",temp.val
                if temp!=None and temp.left !=None:
                    print "add left",temp.left
                    queue.append(temp.left)
                if temp!=None and temp.right != None:
                    print "add right",temp.right
                    queue.append(temp.right)
            print "append l",len_queue
            res.append(l)
        return res


if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    c.l = TreeNode(15)
    c.r = TreeNode(7)
    a.l = b
    a.r = c
    s = Solution()
    s.levelOrder1(a)


