class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
def reverseLinkList(head):
    cur = head 
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre 
        pre = cur 
        cur = tmp
    return pre

head = ListNode(4)
head.next = ListNode(2) 
head.next.next = ListNode(3)

res = reverseLinkList(head)
print(res.val)

        
        