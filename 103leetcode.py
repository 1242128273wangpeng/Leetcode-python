class Solution:
    def __init__(self):
        self.res = []
        self.i = 0
        self.queue = []
        print("zigzag")

    def helper(self,root):
        if root == None:
            return
        self.queue.append(root)
        while self.queue:
            ret = []
            reslen = len(self.queue)
            for i in range(reslen):
                temp = self.queue.pop(0)
                if self.i%2==0:
                    ret.append(temp.val)
                else:
                    ret.insert(0,temp.val)
                if temp!=None and temp.l!= None:
                    self.queue.append(temp.l)
                if temp!=None and temp.r!= None:
                    self.queue.append(temp.r)
            self.res.append(ret)
            self.i+=1

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.l = None
        self.r = None

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.l = b
    a.r = c
    b.l = d
    b.r = e
    c.l = f
    s = Solution()
    s.helper(a)
    print(s.res)
