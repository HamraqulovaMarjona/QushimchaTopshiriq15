
class Node:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_balanced_binary_tree(values):
    if not values:
        return None
    mid = len(values) // 2
    root = Node(values[mid])
    root.left = create_balanced_binary_tree(values[:mid])
    root.right = create_balanced_binary_tree(values[mid+1:])
    return root

def print_tree(root):
    if not root:
        return
    print(root.value)
    print_tree(root.left)
    print_tree(root.right)

values = [88,92,82,24,13,21,33,97,49,18,98,61,57,76,98,97,33]
values.sort()
root = create_balanced_binary_tree(values)
print_tree(root)