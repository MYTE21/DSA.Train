"""
Checking if a binary tree is a full binary tree
"""


# Creating a node
class Node:
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


# Checking full binary tree
def is_full_binary_tree(root):
    # Tree empty case
    if root is None:
        return True

    # Check whether child is present
    if root.left_child is None and root.right_child is None:
        return True

    if root.left_child is not None and root.right_child is not None:
        return is_full_binary_tree(root.left_child) and is_full_binary_tree(root.right_child)

    return False


# Creating binary tree
def create_binary_tree():
    root = Node(1)

    root.right_child = Node(3)
    node_2 = root.left_child = Node(2)

    node_5 = node_2.right_child = Node(5)
    node_2.left_child = Node(4)

    node_5.right_child = Node(7)
    node_5.left_child = Node(6)

    return root


# TODO: Show the binary tree in 2D
def show_binary_tree():
    pass


if __name__ == "__main__":
    root_node = create_binary_tree()
    print("The tree is a full binary tree.") if is_full_binary_tree(root_node) else print("The tree is not a full "
                                                                                          "binary tree")
