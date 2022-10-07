class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left_node(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right_node(self, node):
        self.right = node
        if node is not None:
            node.parent = self


def create_binary_tree():
    # Create Nodes
    two, seven, nine, one, six, eight, five, ten, three, four = TreeNode(2), TreeNode(7), TreeNode(9), TreeNode(1), TreeNode(6), TreeNode(8), TreeNode(5), TreeNode(10), TreeNode(3), TreeNode(4)

    # Create The Binary Tree
    two.add_left_node(seven)
    two.add_right_node(nine)

    seven.add_left_node(one)
    seven.add_right_node(six)

    nine.add_right_node(eight)

    six.add_left_node(five)
    six.add_right_node(ten)

    eight.add_left_node(three)
    eight.add_right_node(four)

    # Return The Binary Tree
    return two


def pre_order_tree(node):
    print(node)

    if node.left:
        pre_order_tree(node.left)
    if node.right:
        pre_order_tree(node.right)


def post_order_tree(node):
    if node.left:
        post_order_tree(node.left)
    if node.right:
        post_order_tree(node.right)

    print(node)


def in_order_tree(node):
    if node.left:
        in_order_tree(node.left)

    print(node)

    if node.right:
        in_order_tree(node.right)


def print_tree_with_parent(node, level=0):
    if node is not None:
        print_tree_with_parent(node.right, level + 1)
        print(" " * 4 * level + "-> " + str(node.data) + "(" + str(node.parent) + ")")
        print_tree_with_parent(node.left, level + 1)


if __name__ == "__main__":
    root = create_binary_tree()                # Creat Binary Tree
    print_tree_with_parent(root)               # Print The Binary Tree with Parent
    pre_order_tree(root)                       # Traverse Pre-Order
    post_order_tree(root)                      # Traverse Post Order
    in_order_tree(root)                        # Traverse In-Order