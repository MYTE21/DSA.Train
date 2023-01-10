class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self


def bst_insert(root, node):
    last_node = None
    current_node = root

    while current_node is not None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right

    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)

    return root


def create_bst():
    root = TreeNode(10)

    for item in [5, 17, 3, 7, 12, 19, 1, 4]:
        node = TreeNode(item)
        root = bst_insert(root, node)

    return root


# * Printing the Binary Tree in Ascending Order using 'In-Order Traversal'
def in_order(node):
    if node.left:
        in_order(node.left)

    print(node)

    if node.right:
        in_order(node.right)


def bst_search(node, key):
    while node is not None:
        if node.data == key:
            return node
        if key < node.data:
            node = node.left
        else:
            node = node.right

    return node


# Smallest Number
def bst_minimum(root):
    while root.left is not None:
        root = root.left

    return root


def bst_transplant(root, current_node, new_node):
    if current_node.parent is None:
        root = new_node
    elif current_node == current_node.parent.left:
        current_node.parent.add_left(new_node)
    else:
        current_node.parent.add_right(new_node)

    return root


def bst_delete(root, node):
    if node is not None:
        if node.left is None:
            root = bst_transplant(root, node, node.right)
        elif node.right is None:
            root = bst_transplant(root, node, node.left)
        else:
            min_node = bst_minimum(node.right)
            if min_node.parent != node:
                root = bst_transplant(root, min_node, min_node.right)
                min_node.add_right(node.right)
            root = bst_transplant(root, node, min_node)
            min_node.add_left(node.left)

    return root


if __name__ == "__main__":
    root_node = create_bst()
    print("Root node of the BST: ", root_node)
    print("BST in Ascending order: ")
    in_order(root_node)

    # Smallest Number in the Binary Search Tree
    smallest_number = bst_minimum(root_node)
    print("Smallest Number: ", smallest_number)

    # Search elements in the Binary Search Tree
    for ele in [1, 5, 10, 7, 8]:
        print("Searching: ", ele)
        result_node = bst_search(root_node, ele)
        print(f"Found {ele}: ", bool(result_node))
        print("Will delete: ", result_node)
        root_node = bst_delete(root_node, result_node)
        print("Updated BST (Ascending): ")
        in_order(root_node)