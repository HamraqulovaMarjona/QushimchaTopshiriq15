
from collections import deque

class Node:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_full_binary_tree(values):
    if not values:
        return None
    root = Node(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()
        node.left = Node(values[i])
        queue.append(node.left)
        i += 1
        if i < len(values):
            node.right = Node(values[i])
            queue.append(node.right)
            i += 1
    return root

def print_tree(root):
    if not root:
        return
    print(root.value)
    print_tree(root.left)
    print_tree(root.right)

values = [88,92,82,24,13,21,33,97,49,18,98,61,57,76,98,97,33]
root = create_full_binary_tree(values)
print_tree(root)