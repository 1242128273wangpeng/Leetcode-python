# coding=utf-8
import copy
class TreeNode:
    def __init__(self,v):
        self.left = None
        self.right = None
        self.val = v

class Solution:
    def __init__(self):
        print("257leetcode")
    
    def allpath(self,root):
        if root==None:
            return 
        res = list()
        path = list()
        #path.append(root.val)
        path = path+[root.val]
        return self.solve(res,path,root)
    # dfs 递归
    def solve(self,res,path,root):
        if root==None:
            return
        if root.left==None and root.right==None:
            res.append(path)
        else:
            if root.left!=None:
                self.solve(res,path+[root.left.val],root.left)
            if root.right!=None:
                self.solve(res,path+[root.right.val],root.right)
        return res
   
    # dfs 栈的非递归
    def dfs(self,root):
        if root == None:
            return 
        q = list()
        nodes = list()
        q.append(str(root.val))
        nodes.append(root)
        res = list()
        while nodes:
            t = nodes.pop()
            qt = q.pop()
            print("qt",qt,"q",q)
            if t.left==None and t.right==None:
                res.append(copy.copy(qt))
            else:
                if t.left!=None:
                    q.append(str(qt)+"->"+str(t.left.val))
                    nodes.append(t.left)
                if t.right!=None:
                    q.append(str(qt)+"->"+str(t.right.val))
                    nodes.append(t.right)
        return res

    # bfs 队列实现
    def bfs(self,root):
        if root==None:
            return 
        res = list()
        qv = list()
        q = list()
        qv.append(root.val)
        q.append(root)
        while q:
            t = q.pop(0)
            tv = qv.pop(0)
            if t.left==None and t.right==None:
                res.append(tv)
            else:
                if t.left!=None:
                    qv.append(str(tv)+"->"+str(t.left.val))
                    q.append(t.left)
                if t.right!=None:
                    qv.append(str(tv)+"->"+str(t.right.val))
                    q.append(t.right)
        return res




if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    s = Solution()
    #print s.allpath(a)
    print(s.bfs(a))
