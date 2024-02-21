class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.val:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def iterative_inorder_traversal(self):
        stack, result = [], []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

# Example usage

bst = BinarySearchTree()
bst.insert(5)
bst.insert(6)
bst.insert(2)
bst.insert(1)
bst.insert(8)
bst.insert(10)
bst.insert(9)
bst.insert(4)
bst.insert(7)
print("Found" if bst.search(7) else "Not Found")
# Found


print("Inorder Traversal:", bst.iterative_inorder_traversal())
