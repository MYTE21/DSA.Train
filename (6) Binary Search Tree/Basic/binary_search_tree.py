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


if __name__ == "__main__":
    root_node = create_bst()
    print("Root node of the BST: ", root_node)
    print("Ascending order of the BST: ")
    in_order(root_node)

    # Search elements in the Binary Search Tree
    for item in [7, 8]:
        print("Searching: ", item)
        result = bst_search(root_node, item)
        print(result)