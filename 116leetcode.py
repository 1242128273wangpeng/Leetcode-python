class Solution:
    def __init__(self):
        print("leetcode 116")


    def solve(self):
        if root!=None:
            temp_list=[root]
            new_list=[root]
            while True:
                new_list=[]
                while temp_list!=[]:
                    temp_node=temp_list.pop(0)
                    new_list.append(temp_node.left)
                    new_list.append(temp_node.right)

                if new_list[0]==None:
                    break

                for i in range(len(new_list)-1):
                    new_list[i].next=new_list[i+1]

                temp_list=new_list


if __name__ == "__main__":
    s = Solution()
    s.solve()
