# [3,2,1,4,7,5]
# heapify to maintain a large heap  root > left > right
#   3
#  / \
# 2   1
#/ \  /\
#4 7  5
#   1
#  / \
#[2] [3]
#/ \  /\
#[4] [5]  [7] cut
#################

def heapify(heap,idx,length):

    curr_idx = idx
    root_idx = idx
    left_idx = 2*idx + 1
    right_idx = 2*idx + 2

    if left_idx < length and heap[curr_idx] < heap[left_idx]:
        curr_idx = left_idx
    if right_idx< length and heap[curr_idx] < heap[right_idx]:
        curr_idx = right_idx

    if curr_idx != root_idx:
        heap[curr_idx],heap[root_idx] = heap[root_idx],heap[curr_idx]
        heapify(heap,curr_idx,length)

def heap_build(heap):
    length = len(heap) # build heap first time
    for i in range((length)//2,-1,-1): # ???
        heapify(heap,i,length)
    print(heap)

def heap_sort(heap):
    length = len(heap)
    heap_build(heap)
    for j in range(length-1,-1,-1): #!!!
        print(heap)
        heap[j], heap[0] = heap[0],heap[j] # cut the largest one build new heap
        print(heap)
        heapify(heap,0,j)
    return heap

print(heap_sort([3,17,1,4,7,5,8,9,44,1]))
#print(heap_build([6,7,3,2,8,9,12]))
#########################################################
# min-heap: root will be the smallest value of current subtree top is the smallest
# max-heap: root will be the larger than its children  top is the largest
# heapify will maintain the heap as max-heap ot min-heap
# how to implement heapify

# class min_heap():
#     def __init__(self,size):
#         self.list = []
#         self.size = size

#     def insert(self,v):

#         if len(self.list) < self.size:
#             self.list.append(v)
#             self.shift_up()
#         else:
#             print('your heap is full')
#         print('you have inserted a value to the heap')
#     def shift_up(self):
#         curr_size = len(self.list)
#         for i in range(curr_size//2 - 1,-1,-1):
#             cur_smaller = i
#             if 2*i < curr_size: # if left child exist
#                 if self.list[2*i] < self.list[cur_smaller]:
#                     cur_smaller = 2*i
#             if 2*i + 1 < curr_size:
#                 if self.list[2*i+1] < self.list[cur_smaller]:
#                     cur_smaller = 2* i + 1
#             if cur_smaller != i:
#                 self.list[i],self.list[cur_smaller] = self.list[cur_smaller],self.list[i]


#     def find_min(self):
#         print(self.list[0])
#         return self.list[0]

#     def cur_size(self):
#         return len(self.list)
#     def pop_min_out(self):
#         self.list.pop(0)
#         self.shift_up()
#         print(self.list)

# h=min_heap(10)
# h.insert(4)
# h.insert(5)
# h.insert(12)
# h.insert(45)
# h.insert(21)
# h.insert(14)
# h.insert(2)
# h.insert(13)
# h.insert(2)

# h.find_min()
# h.pop_min_out()
# h.pop_min_out()




