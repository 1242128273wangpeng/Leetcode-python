class TreeNode:
    def __init__(self,val):
        self.v = val
        self.l = None
        self.r = None

def helper(root):
    if root is None:
        return 0
    else:
        l_size = helper(root.l)
        r_size = helper(root.r)
        if abs(l_size-r_size)>1:
            return -1
        else:
            return max(l_size,r_size)+1

def solution(root):
    if root is None:
        return
    else:
        return helper(root)

if __name__=="__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.l = b 
    a.r = c
    b.l = TreeNode(4)
    b.r = TreeNode(5)
    c.l = TreeNode(7)
    print("solution",solution(a)>0)
    
