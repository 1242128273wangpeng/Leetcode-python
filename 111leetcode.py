class TreeNode:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.var = x


def solution(root):
    if root == None:
        return 0
    queue = list()
    level = 0
    queue.append(root)
    res = []
    while queue:
        q_len = len(queue)
        print("len",q_len)
        temp = list()
        for i in range(0,q_len):
            node = queue.pop(0)
            temp.append(node.var)
            print("node",node.var)
            if node.left==None and node.right==None:
                print("level",level ,node.var)
                return level
            if node.left!=None:
                queue.append(node.left)
                print("add left",node.left.var)
            if node.right!=None:
                queue.append(node.right)
                print("add right",node.right.var)
        res.append(temp)
        print(res)
        level+=1
    return level

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    f = TreeNode(5)
    g = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = f
    c.left = None
    c.right = g
    print(solution(a))



