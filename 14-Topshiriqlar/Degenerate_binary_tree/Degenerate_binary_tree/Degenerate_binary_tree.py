
class Node:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_degenerate_binary_tree(values):
    if not values:
        return None
    root = Node(values[0])
    current = root
    for value in values[1:]:
        current.right = Node(value)
        current = current.right
    return root

def print_tree(root):
    if not root:
        return
    print(root.value)
    print_tree(root.left)
    print_tree(root.right)

values = [88,92,82,24,13,21,33,97,49,18,98,61,57,76,98,97,33]
root = create_degenerate_binary_tree(values)
print_tree(root)