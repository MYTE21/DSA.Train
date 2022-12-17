class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node


def create_binary_tree():
    # Create Nodes
    two, seven, nine, one, six, eight, five, ten, three, four = Node(2), Node(7), Node(9), Node(1), Node(6), Node(8), Node(5), Node(10), Node(3), Node(4)

    # Create The Binary Tree
    two.add_left(seven)
    two.add_right(nine)

    seven.add_left(one)
    seven.add_right(six)

    nine.add_right(eight)

    six.add_left(five)
    six.add_right(ten)

    eight.add_left(three)
    eight.add_right(four)

    # Return The Binary Tree
    return two


def pre_order(node):
    print(node)

    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)

    print(node)


def in_order(node):
    if node.left:
        in_order(node.left)

    print(node)

    if node.right:
        in_order(node.right)


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(" " * 4 * level + "-> " + str(node.data))
        print_tree(node.left, level + 1)


if __name__ == "__main__":
    root = create_binary_tree()    # Creat Binary Tree
    print_tree(root)               # Print The Binary Tree
    pre_order(root)                # Traverse Pre-Order
    post_order(root)               # Traverse Post Order
    in_order(root)                 # Traverse In-Order