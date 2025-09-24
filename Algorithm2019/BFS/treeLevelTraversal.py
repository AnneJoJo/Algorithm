from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque([root])  # 使用 deque 优化队列操作
        
        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):
                current_node = queue.popleft()  # O(1) 操作
                level_values.append(current_node.val)
                
                # 简化子节点入队逻辑
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            result.append(level_values)
        
        return result