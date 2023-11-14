class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root

    def pre_order(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=" ")

    def level_order(self, root):
        if root is None:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


bt = BinaryTree()
root = None
values = [50, 30, 20, 40, 70, 60, 80]
for value in values:
    root = bt.insert(root, value)

print("Pre-order traversal:")
bt.pre_order(root)
print("\nPost-order traversal:")
bt.post_order(root)
print("\nIn-order traversal:")
bt.in_order(root)
print("\nLevel-order traversal:")
bt.level_order(root)
