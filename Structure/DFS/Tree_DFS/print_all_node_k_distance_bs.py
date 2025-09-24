# Given a binary tree, a target node in the binary tree, and an integer value k,
# print all the nodes that are at distance k from the given target node. No parent pointers are available.
# 难点： 回溯访问过的点，左右子树要分类讨论 if the tagert node is the left child of the parent check right sibliings
# otherwise check the opposite. until we find the node we want return
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def find_node_top_to_down(root,target,k):

    if root == None:
        return -1
    if root == target:
        find_k_distance_left_right(root,k) # find left and right node with k distance
        return 0


    dl = find_node_top_to_down(root.left,target,k)
    if dl != -1:
        if dl + 1 == k:
            print(root.val)
            return
        else:
            find_k_distance_left_right(root.right,k-dl-2)

        return dl + 1

    dr = find_node_top_to_down(root.right,target,k)

    if dr != -1:
        if dr + 1 == k:
            print(root.val)
            return
        else:
            find_k_distance_left_right(root.left,k-dr-2)
        return dr + 1

    return -1

def find_k_distance_left_right(root,k):

    if root == None:
        return
    if k == 0:
        print(root.val)
    find_k_distance_left_right(root.left,k-1)
    find_k_distance_left_right(root.right,k-1)

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right
find_node_top_to_down(root,target,2)


# Python program to print nodes at distance k from a given node

# A binary tree node
# class Node:
#     # A constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# # Recursive function to print all the nodes at distance k
# # int the tree(or subtree) rooted with given root. See
# def printkDistanceNodeDown(root, k):
#     # Base Case
#     if root is None or k < 0:
#         return
#
#     # If we reach a k distant node, print it
#     if k == 0:
#         print root.data
#         return
#
#     # Recur for left and right subtee
#     printkDistanceNodeDown(root.left, k - 1)
#     printkDistanceNodeDown(root.right, k - 1)
#
#
# # Prints all nodes at distance k from a given target node
# # The k distant nodes may be upward or downward. This function
# # returns distance of root from target node, it returns -1
# # if target node is not present in tree rooted with root
# def printkDistanceNode(root, target, k):
#     # Base Case 1 : IF tree is empty return -1
#     if root is None:
#         return -1
#
#     # If target is same as root. Use the downward function
#     # to print all nodes at distance k in subtree rooted with
#     # target or root
#     if root == target:
#         printkDistanceNodeDown(root, k)
#         return 0
#
#     # Recur for left subtree
#     dl = printkDistanceNode(root.left, target, k)
#
#     # Check if target node was found in left subtree
#     if dl != -1:
#
#         # If root is at distance k from target, print root
#         # Note: dl is distance of root's left child
#         # from target
#         if dl + 1 == k:
#             print root.data
#
#         # Else go to right subtreee and print all k-dl-2
#         # distant nodes
#         # Note: that the right child is 2 edges away from
#         # left chlid
#         else:
#             printkDistanceNodeDown(root.right, k - dl - 2)
#
#         # Add 1 to the distance and return value for
#         # for parent calls
#         return 1 + dl
#
#     # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE
#     # Note that we reach here only when node was not found
#     # in left subtree
#     dr = printkDistanceNode(root.right, target, k)
#     if dr != -1:
#         if (dr + 1 == k):
#             print root.data
#         else:
#             printkDistanceNodeDown(root.left, k - dr - 2)
#         return 1 + dr
#
#     # If target was neither present in left nor in right subtree
#     return -1
#
#
# # Driver program to test above function
# root = Node(20)
# root.left = Node(8)
# root.right = Node(22)
# root.left.left = Node(4)
# root.left.right = Node(12)
# root.left.right.left = Node(10)
# root.left.right.right = Node(14)
# target = root.left.right
# printkDistanceNode(root, target, 2)
#
# # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
