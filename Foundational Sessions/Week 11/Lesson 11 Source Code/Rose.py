class RoseTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class RoseTree:
    def insert(self, parent, child_value):
        child = RoseTreeNode(child_value)
        parent.children.append(child)
        return child

    def search(self, node, key):
        if node.value == key:
            return node
        for child in node.children:
            found = self.search(child, key)
            if found:
                return found
        return None

# Example usage
root = RoseTreeNode('Project A')
rose_tree = RoseTree()
task1 = rose_tree.insert(root, 'Task 1')
rose_tree.insert(task1, 'Subtask 1')
print("Found" if rose_tree.search(root, 'Subtask 1') else "Not Found")
