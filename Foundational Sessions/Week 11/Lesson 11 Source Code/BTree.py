class BTreeNode:
    """Node of a B-Tree"""
    def __init__(self, order):
        self.keys = []
        self.children = []
        self.order = order
        self.is_leaf = True

class BTree:
    """B-Tree structure"""
    def __init__(self, order):
        self.root = BTreeNode(order)
        self.order = order

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.order - 1:
            temp = BTreeNode(self.order)
            temp.children.insert(0, self.root)
            self._split_child(temp, 0)
            self._insert_non_full(temp, key)
            self.root = temp
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.is_leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.order - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i):
        order = self.order
        y = parent.children[i]
        z = BTreeNode(order)
        z.is_leaf = y.is_leaf
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys[order - 1])
        z.keys = y.keys[order: (2 * order - 1)]
        y.keys = y.keys[0: (order - 1)]
        if not y.is_leaf:
            z.children = y.children[order: (2 * order)]
            y.children = y.children[0: order]

    def search(self, k, x=None):
        """Search key k in the tree"""
        if not x:
            x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return (x, i)
        if x.is_leaf:
            return None
        return self.search(k, x.children[i])

# Example usage
btree = BTree(3)
btree.insert(5)
btree.insert(6)
btree.insert(1)
btree.insert(8)
btree.insert(10)
btree.insert(9)
btree.insert(4)
btree.insert(7)
found = btree.search(7)
print("Found" if found else "Not Found")
# Found

