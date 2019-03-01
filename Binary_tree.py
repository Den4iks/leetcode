class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if self.data < data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if self.data > data:
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
            print(max(left_height, right_height) + 1)
            return max(left_height, right_height) + 1


node = Node(4)
node.insert(2)
node.insert(7)
node.insert(1)
node.insert(3)
node.insert(6)
node.insert(9)
node.printTree()
