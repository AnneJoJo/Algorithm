class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
def findKth(cur, k):
    while cur and k > 0:
        k-=1
        cur = cur.next
    return cur
        
def reverseListWithKNodes(head, k):
    if not head: return None
    dummy = ListNode(0, head)
    groupPre = dummy
    while True:
        kth = findKth(groupPre, k)
        if not kth:
            break
        tmpStart = groupPre.next
        tmpEnd = kth.next
        pre = groupPre 
        while tmpEnd != tmpStart:
            cut = tmpStart.next
            tmpStart.next = pre 
            pre = tmpStart
            tmpStart = cut
        rest = kth.next
        oldStart = groupPre.next
        groupPre.next = kth
        oldStart.next = rest
    return dummy.next
         
        
        
            
    
    
        
        
        
            
        
        
        
    