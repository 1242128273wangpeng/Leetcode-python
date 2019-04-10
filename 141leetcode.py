class Node:
    def __init__(self,value):
       self.value = value
       self.next = None

class Solution:
    def __init__(self):
        print "141leetcode"
       
    def solve(self,head):
        if head==None or head.next==None or head.next.next==None:
            return False
        else:
            slow = head.next
            fast = head.next.next
            while fast.value!=slow.value:
                if slow.next==None or fast.next.next==None:
                    return False
                slow = slow.next
                fast = fast.next.next
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
    print s.solve(a)


            
        
