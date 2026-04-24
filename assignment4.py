from collections import deque


# ------------------ BST ------------------
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def insert(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def min_value(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Case 1 & 2
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3
            temp = self.min_value(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root


# ------------------ GRAPH ------------------
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 3)],
    'C': [('E', 1), ('F', 8)],
    'D': [('F', 5)],
    'E': [('D', 2), ('F', 6)],
    'F': []
}


def print_graph():
    print("\nAdjacency List:")
    for node in graph:
        print(node, "->", graph[node])


def bfs(start):
    visited = set()
    q = deque([start])
    visited.add(start)  # FIX: mark visited early

    print("\nBFS:", end=" ")

    while q:
        node = q.popleft()
        print(node, end=" ")

        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


def dfs(node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor, _ in graph.get(node, []):
            dfs(neighbor, visited)


# ------------------ HASH TABLE ------------------
class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size  # FIX: supports all key types

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

    def display(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")


# ------------------ MAIN ------------------
if __name__ == "__main__":

    # BST
    bst = BST()
    root = None

    print("BST Operations:")
    nums = [50, 30, 70, 20, 40, 60, 80]
    for n in nums:
        root = bst.insert(root, n)

    print("Inorder:", end=" ")
    bst.inorder(root)

    print("\nSearch 20:", bst.search(root, 20))
    print("Search 90:", bst.search(root, 90))

    print("\nDelete Leaf (20):")
    root = bst.delete(root, 20)
    bst.inorder(root)

    root = bst.insert(root, 65)
    print("\n\nDelete One Child (60):")
    root = bst.delete(root, 60)
    bst.inorder(root)

    print("\n\nDelete Two Children (30):")
    root = bst.delete(root, 30)
    bst.inorder(root)

    print("\n")

    # GRAPH
    print_graph()
    bfs('A')

    print("\nDFS:", end=" ")
    dfs('A')

    print("\n")

    # HASH TABLE
    ht = HashTable(5)

    keys = [10, 15, 20, 7, 12]
    for k in keys:
        ht.insert(k, f"Value{k}")

    ht.display()

    print("\nGet 15:", ht.get(15))
    print("Get 7:", ht.get(7))
    print("Get 20:", ht.get(20))

    print("\nDelete key 15:")
    ht.delete(15)
    ht.display()