class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
            return root

    def pre_order(self, root):
        if root:
            print(root.val, end=' ')
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.val, end=' ')

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.val, end=' ')
            self.in_order(root.right)

    def level_order(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

bt = BinaryTree()
root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = bt.insert(root, key)

print("Pre-order traversal:")
bt.pre_order(root)
print("\nPost-order traversal:")
bt.post_order(root)
print("\nIn-order traversal:")
bt.in_order(root)
print("\nLevel-order traversal:")
bt.level_order(root)