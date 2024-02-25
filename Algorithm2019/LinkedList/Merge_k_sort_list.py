# for the linkList problem always be caution about dummy head
class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None


def merge_k_sort_list(arr):
    """
    we ar gonna use heap to solve this prob
    :param arr: contains several linklist
    :return: the merged list 
    """
  
    if arr == [] or len(arr) == 0:
        return None
    from heapq import heapify, heappop,heappush
    head = res = ListNode(0)

    heap = []
    for each_list in arr:
        heappush(heap,(each_list.val,each_list))

    heapify(heap)
    while heap:
        cur_val, cur_node = heappop(heap)
        res.next = ListNode(cur_val)
        res = res.next
        cur_node = cur_node.next
        if cur_node:
            heappush(heap,(cur_node.val,cur_node))

    return head.next

list1 = ListNode(0)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

list2 = ListNode(0)
list2.next = ListNode(4)
list2.next.next = ListNode(5)

ret = merge_k_sort_list([list1.next,list2.next])

while ret:
    print(ret.val)
    ret = ret.next






