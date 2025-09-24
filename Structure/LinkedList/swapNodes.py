class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapNodes(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        
        # Find node1 (kth node from start) and prev1
        prev1 = dummy
        curr = dummy.next
        count = 1
        while curr and count < k:
            prev1 = curr
            curr = curr.next
            count += 1
        node1 = curr
        if not node1:
            return head
        
        # Find the length of the list
        length = 0
        curr = dummy.next
        while curr:
            length += 1
            curr = curr.next
        
        # Find node2 (kth node from end) and prev2
        target_pos = length - k + 1
        if target_pos < 1:
            return head
        prev2 = dummy
        curr = dummy.next
        count = 1
        while curr and count < target_pos:
            prev2 = curr
            curr = curr.next
            count += 1
        node2 = curr
        if not node2:
            return head
        
        if node1 == node2:
            return dummy.next
        
        # Check if nodes are adjacent
        if node1.next == node2:
            # node1 is immediately before node2
            prev1.next = node2
            node1.next = node2.next
            node2.next = node1
        elif node2.next == node1:
            # node2 is immediately before node1
            prev2.next = node1
            node2.next = node1.next
            node1.next = node2
        else:
            # General case: swap previous nodes' next and adjust next pointers
            prev1.next, prev2.next = node2, node1
            node1.next, node2.next = node2.next, node1.next
        
        return dummy.next