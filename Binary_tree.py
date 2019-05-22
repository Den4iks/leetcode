class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        print(self.data)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()


    def maxDepth(self,data):
        """
        :type root: TreeNode
        :rtype: int
        """
        if data is None:
            return 0
        else:
            left_height = self.maxDepth(data.left)
            right_height = self.maxDepth(data.right)
            return max(left_height, right_height) + 1

    def lowestCommonAncesetor(self,root,p,q):
        if p > root.data and q > root.data:
            return self.lowestCommonAncesetor(root.right,p,q)
        if p < root.data and q < root.data:
            return self.lowestCommonAncesetor(root.left,p,q)
        if p < root.data and q > root.data or q == root.data or p== root.data:
            return root.data

    def reverseTree(self,root):
        queue = [root]
        while len(queue) > 0:
            root_n = queue.pop()
            if root_n is None or root_n.left == root_n.right:
                continue
            cache = root_n.left
            root_n.left = root_n.right
            root_n.right = cache
            if root_n.left is not None: queue.append(root_n.left)
            if root_n.right is not None: queue.append(root_n.right)
        return root

    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q


    def inorderTraversal(self, root):
        ans = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans.append(tmpNode.data)
                root = tmpNode.right

        return ans


node = Node(6)
node.insert(3)
node.insert(8)
node.insert(2)
node.insert(1)
node.insert(4)
node.insert(7)
node.insert(9)
node.insert(5)
node.insert(22)
node.inorderTraversal(node)
