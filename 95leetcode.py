class TreeNode:
    def __init__(self,v):
        self.left = None
        self.right = None
        self.val = v

class Solution:
    def generateTrees(self,n):
        if n == 0:
            return list()
        return self._generateTrees(1,n)

    def _generateTrees(self,left,right):
        if left>right:
            print("None left:",left,"right:",right)
            return [None]
        res = list()
        r = right+1
        print(left,r)
        for i in range(left,r):
            print("i:",i)
            left_nodes = self._generateTrees(left,i-1)
            print("l  left",left,"r",i-1,"len:",len(left_nodes))
            right_nodes = self._generateTrees(i+1,right)
            print("r  left",i+1,"r",right,"len:",len(right_nodes))
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    if left_node==None:
                        print("left_node is null")
                    else:
                        print("left_node:",left_node.val)
                    root.right = right_node
                    if right_node==None:
                        print("right_node is null")
                    else:
                        print("right_node:",right_node.val)
                    res.append(root)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.generateTrees(3))

