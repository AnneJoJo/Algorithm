#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postOrderNoRecursive(root):
    stackNode = []
    stack = []
    node = root
    res = []
    stack.append(node)
    while stack:
        cur = stack.pop()
        stackNode.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
            
    return stackNode[::-1]

root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(6)
print(postOrderNoRecursive(root))
    