import timeit

class Node:
    """A Node in the Binary Search Tree."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new node into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.val == key:
            return node is not None
        if key < node.val:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self, node):
        """Perform an inorder traversal of the BST."""
        if node:
            yield from self.inorder_traversal(node.left)
            yield node.val
            yield from self.inorder_traversal(node.right)

# Performance Analysis
def test_performance():
    small_tree = BST()
    large_tree = BST()
    
    small_data = [5, 3, 7, 2, 4, 6, 8]
    large_data = list(range(1, 10001))
    
    for num in small_data:
        small_tree.insert(num)
    for num in large_data:
        large_tree.insert(num)
    
    # Measure search time
    small_tree_time = timeit.timeit(lambda: small_tree.search(4), number=1000)
    large_tree_time = timeit.timeit(lambda: large_tree.search(5000), number=1000)
    
    print("Search Performance:")
    print(f"Small Tree (7 nodes) search time: {small_tree_time:.6f} sec")
    print(f"Large Tree (10,000 nodes) search time: {large_tree_time:.6f} sec")

if __name__ == "__main__":
    test_performance()
