class TreeNode:
    def __init__(self,x=None):
        self.left = None
        self.right = None
        self.val = x

def createTree(root,arr):
    return helper(root,arr,0)
    print "sort",arr
        
def helper(root,arr,i):
    if i<len(arr):
        if arr[i]=="#":
            return None
        else:
            root = TreeNode(arr[i])
            print "helper",arr[i]
            root.left = helper(root.left,arr,2*i+1)
            root.right = helper(root.right,arr,2*i+2)
            return root
    return root

def preTraversal(root):
    if root == None:
        print "none"
        return
    else:
        print root.val
        preTraversal(root.left)
        preTraversal(root.right)

def find(root,reslist,total,nowlist):
    print "root.val",root.val,"total",total,"now",nowlist
    if root==None:
        return reslist
    else:
        if root.left==None and root.right==None and total==0:
            reslist.append(nowlist)
        if root.left!=None:
            find(root.left,reslist,total-int(root.left.val),nowlist+[int(root.left.val)])
        if root.right!=None:
            find(root.right,reslist,total-int(root.right.val),nowlist+[int(root.right.val)])
    return reslist




if __name__ == "__main__":
    root = TreeNode()
    arr = ["1","2","3","#","4","5"]
    root = createTree(root,arr)
    preTraversal(root)
    print find(root,[],9-int(root.val),[int(root.val)])


