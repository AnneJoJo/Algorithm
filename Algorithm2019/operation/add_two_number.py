class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def add_two_number(self,l1,l2):
        # 2 -> 4 -> 3
        # 5 -> 6 -> 4

        carry_bit = 0
        pos_sum = 0
        head = Node(0)
        new_list = head
        while l1 != None or 2 != None:
            if l1 and l2:
                pos_sum = l1.val + l2.val + carry_bit
                l1 = l1.next
                l2 = l2.next

            elif l1:
                pos_sum = l1.val + carry_bit
                l1 = l1.next

            elif l2:
                pos_sum = l2.val + carry_bit
                l2 = l2.next

            carry_bit = pos_sum // 10
            cur_node = Node(pos_sum % 10)
            new_list.next = cur_node
            new_list = new_list.next

        if carry_bit > 0:
            first = Node(carry_bit)
            new_list.next = first
        return head.next

# follow up what if reverse the linkList
# what if the input is string



