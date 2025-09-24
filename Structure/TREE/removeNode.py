# class Solution {
# public:
#     unordered_set<int>s;
#     vector<TreeNode*>ans;
#     void dfs(TreeNode* &root) {
#         if(!root) return;
#         dfs(root->left), dfs(root->right);
#         if(s.find(root->val) != s.end()) {
#             if(root->left) ans.push_back(root->left);
#             if(root->right) ans.push_back(root->right);
#             root = NULL;
#         }
#     }
#     vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
#         for(auto c : to_delete) s.insert(c);
#         dfs(root);
#         if(root) ans.push_back(root);
#         return ans;
#     }
# };

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
        def dfsFind(node, delet):
            if not node:
                return None
            ret1, ret2 = None, None
            
            ret1 = dfsFind(node.left, delet) 
            ret2 = dfsFind(node.right, delet)
            if node.val in delet:
                if ret1:
                    self.forest.append(ret1)
                if ret2:
                    self.forest.append(ret2)
                delet.remove(node.val)
                return None
            node.left = ret1
            node.right = ret2
            return node
            
        self.forest = []
        rootTrim =  dfsFind(root, to_delete)
       
        if rootTrim:
            self.forest.append(rootTrim)
        
        return self.forest
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
        def dfsFind(node, delet):
            if not node:
                return None
            ret1, ret2 = None, None
            if node.val in delet: 
                
                if node.left:
                    depNodeL = dfsFind(node.left, delet)
                    node.left = depNodeL
                    if node.left:
                        self.forest.append(node.left)
                    node.left = None
                if node.right:
                    depNodeR = dfsFind(node.right, delet)
                    node.right = depNodeR
                    if node.right:
                        self.forest.append(node.right)
                    
                    node.right = None
                delet.remove(node.val)
                return None
            
            ret1 = dfsFind(node.left, delet) 
            ret2 = dfsFind(node.right, delet)
            node.left = ret1
            node.right = ret2
            return node
            
        self.forest = []
        rootTrim =  dfsFind(root, to_delete)
       
        if rootTrim:
            self.forest.append(rootTrim)
        
        return self.forest