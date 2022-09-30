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
    """
    Create Binary Tree
         _2_
       /    \
      7      9
     / \      \
    1   6      8
       / \   /  \
      5  10 3    4
    input: None
    return: The Binary Tree
    """
    # Create Nodes
    two, seven, nine, one, six, eight, five, ten, three, four = \
        Node(2), Node(7), Node(9), Node(1), Node(6), Node(8), Node(5), Node(10), Node(3), Node(4)

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


if __name__ == "__main__":
    root = create_binary_tree()
    pre_order(root)