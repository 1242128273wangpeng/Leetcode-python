class Node:
    def __init__(self,value):
       self.value = value
       self.next = None

class Solution:
    def __init__(self):
        print("141leetcode")
       
    def solve(self,head):
        if head==None or head.__next__==None or head.next.__next__==None:
            return False
        else:
            slow = head.__next__
            fast = head.next.__next__
            while fast.value!=slow.value:
                if slow.__next__==None or fast.next.__next__==None:
                    return False
                slow = slow.__next__
                fast = fast.next.__next__
            return True

if __name__ == "__main__":
    s = Solution()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = c
    print(s.solve(a))


            
        
