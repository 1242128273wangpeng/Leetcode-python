class TreeNode:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x
        print ""


def solution(root):
    if root == None:
        return 0
    else:
        if root.left!=None and root.right!=None:
            return min(solution(root.left),solution(root.right))+1
        else:
            return max(solution(root.left),solution(root.right))+1

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(1)
    c = TreeNode(1)
    d = TreeNode(1)
    e = TreeNode(1)
    f = TreeNode(1)
    g = TreeNode(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    d.left =f
    d.right = g
    f.left=TreeNode(4)
    print solution(a)


