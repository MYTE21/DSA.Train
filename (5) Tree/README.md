# 🌳 Tree - Binary Tree

### Prerequisites:

* [X]  [Recursion](../(4)%20Recursion)

### Contents:

1. [Tree](#tree)
2. [Binary Tree](#binary-tree)
   1. Create `Node`.
   2. Create `Tree`.
3. [Tree Traverse]()
   1. `Pre-order` traverse.
   2. `Post-order` traverse.
   3. `In-order` traverse.

* **EXTRA**: Tracking Parent Node.

## Tree
<img height="265em" src="../assets/(5) Tree/tree.png" alt="">

## Binary Tree




`If we wanted, 'stack' can be applied instead of 'recursion' for the algorithms.`

Used In: `Tree clone, binary search tree`

How to get the parent node of a node?
➡️

```python
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
```
